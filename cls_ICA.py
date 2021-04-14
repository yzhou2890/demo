


# demo of running [Amari96]

from theano import function, config, shared, sandbox
import theano.tensor as T


import numpy as np
import time

import matplotlib

from matplotlib import pyplot as plt

from matplotlib.animation import FuncAnimation




class ICA():

    def __init__(self,data,nIte=300,eta=0.1,method ='batch'):
        # constructor of this class
        self.X = data
        self.d = data.shape[0]
        self.n = data.shape[1]
        self.ite = nIte
        self.eta = eta
        self.mtd = method
        self.I_dxd = np.eye( self.d,dtype=np.float64)
        self.W0  = np.matrix(np.random.rand( self.d,self.d ),dtype=np.float64)*0.02 - 0.01



    def Amari96_Eqn_14( self, y ):
        vcoeff  = [ 3/4, 15/4,  -14/3,  -29/4,  29/4 ]  # rectified version
        vn      = [ 11,  9,      7,        5,     3  ]
        return np.sum( vcoeff * np.power(y, vn) )



    def Update_W0_single(self):

        Y = self.getResult()
        
        PhiY = np.zeros( Y.shape, dtype=np.float64 )
    
        for j in range(self.d):
            for k in range(self.n):
            
                PhiY[j,k] = self.Amari96_Eqn_14( Y[j,k] )

                self.W0  = self.W0 + self.eta * ( self.I_dxd -  PhiY[j,k]*Y[j,k] ) * self.W0 / self.n**2

        return self.W0




    def Update_W0_batch(self):
        Y    = self.getResult()
        
        PhiY = np.zeros( Y.shape, dtype=np.float64 )

        for j in range(self.d):
            for k in range(self.n):
            
                PhiY[j,k] = self.Amari96_Eqn_14( Y[j,k] )

        self.W0  = self.W0 + self.eta * ( self.I_dxd -  PhiY*np.transpose(Y)/ self.n**4 ) * self.W0


        return self.W0


    def run(self):
        print '='*20, 'start running ICA ', '='*20
        self.display()


    
        t0 = time.time()
        for i in range(self.ite):
            if self.mtd == 'batch':
                self.Update_W0_batch()
            elif self.mtd == 'single':
                self.Update_W0_single()
    
        t1 = time.time()
        print("Looping %d times took %f seconds" % (self.ite, t1 - t0))




    def display(self):
        print 'num of signals   = %d'   % self.d
        print 'samples of a sig = %d'   % self.n
        print 'iteration number = %d'   % self.ite
        print 'learning rate    = %.3f' % self.eta
        print 'learning method  = %s'   % self.mtd
    
    def show(self):
        Y = self.getResult()

        h = plt.figure('results', facecolor='white'  )
        #h.patch.set_facecolor('white')

        for i in range(self.d):
            plt.subplot(self.d,3,3+3*i),
            plt.plot( np.ravel(Y[i,:]), 'b' )
            plt.legend(['ICA result-%d'%(i+1)])

            plt.yticks([])
            if i == 2:
                plt.xlabel('time index')
            else:
                plt.xticks([])
        

        plt.show()


    def getResult(self):
        return self.W0*self.X


def Show_source(Data):

    Y = Data
    
    h = plt.figure('results', figsize=(15,10)  )
    #h.patch.set_facecolor('white')
    h.subplots_adjust(bottom=0.05, left=0.05, top = 0.975, right=0.975)
    
        
    for i in range(Y.shape[0]):
        plt.subplot(Y.shape[0],3,1+3*i),
        plt.plot( np.ravel(Y[i,:]), 'g' )
        
        plt.legend(['source-%d'%(i+1)])
        if i == 2:
            plt.xlabel('time index')
        else:
            plt.xticks([])

    # plt.show()


def Show_mixture(Data):
    
    Y = Data
    
    h = plt.figure('results'  )
    h.patch.set_facecolor('white')
    
    for i in range(Y.shape[0]):
        plt.subplot(Y.shape[0],3,2+3*i),
        plt.plot( np.ravel(Y[i,:]),'r' )
        plt.legend(['mixture-%d'%(i+1)])
        plt.yticks([])
        if i == 2:
            plt.xlabel('time index')
        else:
            plt.xticks([])


    # plt.show()




t = np.linspace(0,1,1000)
S = np.matrix([ np.random.rand(len(t))*2.0 - 1,
                1e-1*np.sin(400*t)*np.cos(30*t),
                1e-3*np.sign( np.sin( 500*t + 9*np.cos(40*t) ))
              ]
            )


A = np.matrix(np.random.rand(3,3), dtype=np.float64)*0.02
X = A*S

Show_source(S)
Show_mixture(X)


cs = ICA(X)
cs.run()
cs.show()







