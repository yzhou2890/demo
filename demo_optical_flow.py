


#------------------------------------
# demo of  optical flow - use [Horn&Schunck,1981]
#------------------------------------
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html
#
#


import numpy as np
import cv2



vcap = cv2.VideoCapture(0)                          # handle for video

nw0 = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)            # frame width
nh0 = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)           # frame height

nheight      = 360;                                 # target frame height
nwidth       = int(nw0 * float(nheight) / nh0 )     # target frame width

vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)          #set width
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)        #set height
vcap.set(cv2.CAP_PROP_FPS,3)                       # frame rate

print( nh0, nw0 )
print(nheight,nwidth)

str = 'WebCam video: Press q to exit >>>'

def capture():
    ret, frame = vcap.read()
    # flip left-right
    frame = cv2.flip(frame, 1)
    
    # Our operations on the frame come here
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    #rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )
    #cv2.imshow(str, rgb)
    
    return rgb
    

def optical_flow_p_c( Previous, Current, alpha, nItr ):
    
    def Gaussian_variants( sigma, nSize ):
        f = (nSize-1)/2;
        vx = np.arange( -f, f, dtype = np.float );
        vy = np.arange( -f, f, dtype = np.float );
    
        for i in

    return



rgb      = capture()
#img_old  = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
img_old  = rgb;
mask     = np.zeros_like( rgb )

while(1):

    # Capture frame-by-frame
    rgb      = capture()
    #img_new  = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    img_new     =   rgb;
    
    # Lucas Kanade
    
    
    # select good points
    
    
    #draw the tracks
    
    
    img = cv2.add(rgb,mask)


    img_old = img_new
    
    # Display the resulting frame
    cv2.imshow(str,img_old)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()


