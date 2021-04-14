
import numpy as np
import matplotlib.pyplot as plt
import time
import cv2


def product(v1,v2):
    y = 0
    for i in range(0,len(v1)):
        y += v1[i]*v2[i]
    return y/len(v1)



if 0:

    v1 = [0, 1, 1]
    v2 = [1, 2, 3]
    v3 = np.random.random((700000,1))
    v4 = np.random.random((700000,1))


    f = product(v1,v2)
    print(f)


if 0:

    h = plt.figure('random numbers')
    h.patch.set_facecolor('white')
    plt.plot(v3[1:20],'ko-')
    plt.show()



if 0:
    plt.ion()

    fig, ax = plt.subplots(1,1)
    #plt.subplot(1,2,1)
    line1,=ax.plot( np.random.rand(100,), 'o' )
    #plt.subplot(1,2,2)
    line2,=ax.plot( np.random.rand(100,), '*')
    #ax.set_autoscalex_on(True)
    #ax.set_autoscaley_on(True)
    #ax.grid()
    
    
    for k in range(100):

        plt.title('k=%d'%k)
        line1.set_ydata( np.random.rand(100,))
        line2.set_ydata( np.random.rand(100,))

        #ax.relim()
        #ax.autoscale_view()
        fig.canvas.draw()
        #fig.canvas.flush_events()

        time.sleep(0.1)




t = np.arange(0, 100, 0.01)
y = np.sin( t )

vx = []
vy = []


if 1:
    plt.ion()
    
    fig, ax = plt.subplots(2,2,sharex=True)
    
    #vx.append( (range(100)))
    #vy.append( (np.random.rand(100)) )
    
    #plt.subplot(1,2,1)
    line1,=ax[0,0].plot( [], 'r.' )
    #plt.title('a')
    
    #plt.subplot(1,2,2)
    line2,=ax[1,1].plot( [], '*' )
    #plt.title('b')
    
    #ax[0,0].set_autoscalex_on(True)
    #ax[0,0].set_autoscaley_on(True)
    ax[0,0].grid()

    #ax[1,1].set_autoscalex_on(True)
    #ax[1,1].set_autoscaley_on(True)
    ax[1,1].grid()
    ax[1,1].set_xlim(0,600)
    ax[1,1].set_ylim(-1,1)


    #fig.patch.set_facecolor('white')
    
    for k in range(100):
        
        n = np.random.randint(100,605)
        print n,
        newx = np.arange(n)
        newy = np.add(np.random.rand(1,n), y[0:n])
        
        if vx ==[]:
            vx, vy = newx, newy
        else:
            vx = np.hstack((vx, newx))
            vy = np.hstack((vy, newy))


        ax[0,0].set_title('k=%d,n=%d'%(k,n))
        line1.set_xdata( newx )
        line1.set_ydata( newy )
        ax[0,0].relim()
        ax[0,0].autoscale_view()
        
        #fig.canvas.draw()
        #fig.canvas.flush_events()


        ax[1,1].set_title('k=%d,n=%d'%(k,n))
        line2.set_xdata( newx )
        line2.set_ydata( y[0:n] )
        ax[1,1].relim()
        ax[1,1].autoscale_view()
        
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        time.sleep(0.001)

