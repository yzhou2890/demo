







#------------------------------------
# demo of simulating DVS - dynamic vision system
#------------------------------------
#


import numpy as np
import cv2

from matplotlib import pyplot as plt


# create random colormap
color = np.random.randint(0,255,(100,3))


vcap = cv2.VideoCapture(0)

nw0 = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
nh0 = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

nwidth       = 320
nheight      = int(nh0 * nwidth / nw0 )
str          = 'demo: Press q to exit >>>'

vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)              #set width
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)            #set height
vcap.set(cv2.CAP_PROP_FPS,30)                            # frame rate


print(nheight,nwidth)
print(vcap.get(cv2.CAP_PROP_FPS))


def capture():
    ret, frame = vcap.read()            # read from camera's buffer

    frame   = cv2.flip(frame, 1)        # flip left-right
    
    gray    = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    rgb     = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )

    return rgb, gray
    

rgb, img_old    = capture()
mask            = np.zeros_like( rgb )

while(1):

    # Capture frame-by-frame
    rgb, img_new  =   capture()


    #
    #diff     = cv2.subtract( img_new, img_old )
    diff      = np.subtract(img_new, img_old)
    #ret,diff = cv2.threshold( diff, 0, 255, cv2.THRESH_OTSU )
    #diff     = np.vstack((img_new, diff))


    hnew,bnew  = np.histogram( img_new.flatten(), 255, [0,255] )
    bnew       = (bnew[0:-1]+bnew[1:])/2
    hdff,bdff  = np.histogram( diff.flatten(), 20, [0,100] )
    bdff       = (bdff[0:-1]+bdff[1:])/2
    ret2,th2   = cv2.threshold( diff, 0, 1, cv2.THRESH_OTSU ) 

    plt.subplot(2,2,1)
    plt.imshow(img_new,cmap='gray')
    plt.subplot(2,2,2)
    plt.plot(bnew, hnew,'b.')
    plt.subplot(2,2,3)
    plt.imshow( th2, cmap = 'gray')
    plt.subplot(2,2,4)
    plt.plot( bdff, hdff, color='b')
    plt.show()

    # cv2.imshow(  "demo - event camera",  diff )
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    '''update before next iteration'''
    img_old  = img_new





# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()


