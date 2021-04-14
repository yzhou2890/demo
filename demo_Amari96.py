


# demo of running [Amari96]

# see cls_ICA.py for a more concise demo of ICA as it is using object-oriented programming


# from theano import function, config, shared, sandbox
# import theano.tensor as T

import numpy as np
import time

from matplotlib import pyplot as plt



vlen  = np.array([3,5000],dtype=np.int32)    # [num_of_signals, len_of_samples]
iters = 300                # num of iterations
eta   = 0.1                 # learning rate
I_dxd = np.eye(vlen[0],dtype=np.float64)



t = np.linspace(0,0.1,vlen[1])
S = np.matrix([np.random.rand(len(t))*2.0 - 1,
               1e-1*np.sin(400*t)*np.cos(30*t),
               1e-2*np.sign( np.sin( 500*t + 9*np.cos(40*t) ))])

A = np.matrix(np.random.rand(3,3),dtype=np.float64)*0.02
X = A*S



def Amari96_Eqn_14( y ):
    vcoeff  = [ 3/4, 15/4,  -14/3,  -29/4,  29/4 ]  # rectified version
    vn      = [ 11,  9,      7,        5,     3  ]
    return np.sum( vcoeff * np.power(y, vn) )



def Update_W0_single(W0, Y):
    
    PhiY = np.zeros( Y.shape, dtype=np.float64 )
    
    for j in range(0,vlen[0]):
        for k in range(0,vlen[1]):
            
            PhiY[j,k] = Amari96_Eqn_14( Y[j,k] )

            W0  = W0 + eta * ( I_dxd -  PhiY[j,k]*Y[j,k] ) * W0 /vlen[1]**2

    return W0




def Update_W0_batch(W0, Y):
    
    PhiY = np.zeros( Y.shape, dtype=np.float64 )

    for j in range(0,vlen[0]):
        for k in range(0,vlen[1]):
            
            PhiY[j,k] = Amari96_Eqn_14( Y[j,k] )

    W0  = W0 + eta * ( I_dxd -  PhiY*np.transpose(Y)/vlen[1]**1.5 ) * W0


    return W0





W0 = np.matrix(np.random.rand( vlen[0],vlen[0] ),dtype=np.float64)*0.02 - 0.01

t0 = time.time()
for i in range(iters):
    W0 = Update_W0_batch(W0, W0*X)
    
    if i%50 == 0:
        print(W0)
    #    W0 = W0 / np.linalg.norm( W0 )

t1 = time.time()





print("Looping %d times took %f seconds" % (iters, t1 - t0))



Y = W0 * X


h = plt.figure('signals',figsize=(6,3),dpi=150  )
h.patch.set_facecolor('white')

for i in range(vlen[0]):
    plt.subplot(3,3,1+3*i),
    plt.plot(np.ravel(S[i,:]))
    plt.subplot(3,3,2+3*i)
    plt.plot(np.ravel(X[i,:] ))
    plt.subplot(3,3,3+3*i)
    plt.plot(np.ravel(Y[i,:]))


plt.show()

print('=============================')
print('==== A  ======')
print(A)
print('==== W0 ======')
print(W0)
print('==== A*W0 ======')
print(A*W0)
print('==== W0*A ======')
print(W0*A,)




