


# demo of running [Amari96]


from theano import function, config, shared, sandbox
import theano.tensor as T


import numpy as np
import time

import matplotlib

from matplotlib import pyplot as plt

from matplotlib.animation import FuncAnimation


fig = plt.figure('ICA Simulation', figsize=(15,8), facecolor='w'  )
#fig.subplots_adjust(bottom=0.075, left=0.05, top = 0.975, right=0.975)


ax3 = fig.add_subplot(333,  autoscale_on = False,  xlim=(0, 1000) )
onax3, = ax3.plot([], [], lw=1)                             # plot holding the restored signal
ax6 = fig.add_subplot(336,  autoscale_on = False,  xlim=(0, 1000) )
onax6, = ax6.plot([], [], lw=1)                             # plot holding the restored signal
ax9 = fig.add_subplot(339,  autoscale_on = False,  xlim=(0, 1000) )
onax9, = ax9.plot([], [], lw=1)                             # plot holding the restored signal



def show_source(S):
    
    Y = S
    
    for i in range(Y.shape[0]):
        plt.subplot(Y.shape[0],3, 1+3*i),
        plt.plot( np.ravel(Y[i,:]), 'g' )
        
        plt.legend(['source-%d'%(i+1)])
        if i == 2:
            plt.xlabel('time index')
        else:
            plt.xticks([])

def show_mixture(X):
    Y = X
    
    handles = np.zeros(3)
    for i in range(Y.shape[0]):
        plt.subplot(Y.shape[0],3, 2+3*i),
        plt.plot( np.ravel(Y[i,:]),'r' )
        plt.legend(['mixture-%d'%(i+1)])
        plt.yticks([])
        if i == 2:
            plt.xlabel('time index')
        else:
            plt.xticks([])




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



    def Update_W0_batch(self):
        Y    = self.getResult()
        
        PhiY = np.zeros( Y.shape, dtype=np.float64 )

        for j in range(self.d):
            for k in range(self.n):
                PhiY[j,k] = self.Amari96_Eqn_14( Y[j,k] )

        self.W0  = self.W0 + self.eta * ( self.I_dxd -  PhiY*np.transpose(Y)/ self.n**2 ) * self.W0

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
        
        
        def init( ):
            show_source(S)
            show_mixture(X)
            
            x = np.linspace(0,self.X.shape[1],self.X.shape[1])
            onax3.set_xdata(x)
            onax6.set_xdata(x)
            onax9.set_xdata(x)
            return onax3, onax6, onax9
        

        def ani( index ):
            h = plt.figure('results', facecolor='white'  )
            
            unit = 5;               # no. of repetitions of each update
            for i in range(unit):
                self.Update_W0_batch()

            Y = self.getResult()
            
            for i in range(self.d):     # update the view within this loop
                y = np.ravel(Y[i,:])
                        
                if i == 0:
                    onax3.set_ydata(y)
                    ax3.set_ylim( np.min(y)*1.2, np.max(y)*1.2)
                    ax3.set_yticks([])
                    ax3.legend(['ICA result-%d/%d'%(i+1,index*unit)])
                
                    ax3.set_xticklabels([])

                if i == 1:
                    onax6.set_ydata(y)
                    ax6.set_ylim( np.min(y)*1.2, np.max(y)*1.2)
                    ax6.set_yticks([])
                    ax6.legend(['ICA result-%d/%d'%(i+1,index*unit)])
                
                    ax6.set_xticklabels([])

                if i == 2:
                    onax9.set_ydata(y)
                    ax9.set_ylim( np.min(y)*1.2, np.max(y)*1.2)
                    ax9.set_yticks([])
                    ax9.legend(['ICA result-%d/%d'%(i+1,index*unit)])

                    ax9.set_yticklabels([])
                    ax9.set_xlabel('time index')

    
            return onax3, onax6, onax9
        
        an = FuncAnimation( fig, ani, init_func = init,   interval=1, blit=False, frames=60)
        plt.show()



    def getResult(self):
        return self.W0*self.X
    

    def __del__(self):
        plt.close()



t = np.linspace(0,1,1000)
S = np.matrix([ np.random.rand(len(t))*2.0 - 1,
               1e-10*np.sin(400*t)*np.cos(30*t),
               1e-10*np.sign( np.sin( 500*t + 9*np.cos(40*t) ))
               ]
              )


A   =   np.matrix(np.random.rand(3,3), dtype=np.float64)*0.02
X   =   A*S
cs  =   ICA(X)


cs.show()

