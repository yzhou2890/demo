


#------------------------------------
# demo of Lucas Kanade - optical flow
#------------------------------------
# http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html
#
#


import numpy as np
import cv2

# parameters for ShiTomasi corner detection
feature_prmtr = dict(maxCorners   = 100,
                     qualityLevel = 0.3,
                     minDistance  = 7,
                     blockSize    = 7 )

# parameters for Lucas Kanade optical flow
lk_prmtr     = dict(winSize  = (15,15),
                    maxLevel = 2,
                    criteria = (cv2.TERM_CRITERIA_EPS|cv2.TERM_CRITERIA_COUNT,10,0.03))

# create random colormap
color = np.random.randint(0,255,(100,3))


vcap = cv2.VideoCapture(0)

nw0 = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
nh0 = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

nwidth       = 320
nheight      = int(nh0 * nwidth / nw0 )

vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)             #set width
vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)             #set height
vcap.set(cv2.CAP_PROP_FPS,30)                       # frame rate


print(nheight,nwidth)

str = 'WebCam video: Press q to exit >>>'

def capture():
    ret, frame = vcap.read()
    # flip left-right
    frame = cv2.flip(frame, 1)
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )
    #cv2.imshow(str, frame)
    
    return rgb, gray
    

rgb, img_old  = capture()
p0       = cv2.goodFeaturesToTrack( img_old, mask=None,**feature_prmtr)
mask     = np.zeros_like( rgb )

while(1):

    # Capture frame-by-frame
    rgb, img_new  =   capture()

    # Lucas Kanade
    p1,st,err = cv2.calcOpticalFlowPyrLK(img_old,img_new,p0,None,**lk_prmtr)
    
    # select good points
    good_new = p1[st==1]
    good_old = p0[st==1]
    
    
    #draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        a,b,c,d = np.int16(a), np.int16(b), np.int16(c), np.int16(d)
        #mask = cv2.line(mask,(a,b),(c,d),color[i].tolist(),2)
        mask = cv2.arrowedLine( mask, (a,b), (c,d), color[i].tolist(),2 )
        rgb  = cv2.circle(rgb,(a,b),5,color[i].tolist(),-1)

    img = cv2.add(rgb,mask)
    
    
    # Display the resulting frame
    cv2.imshow(str,img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    img_old  = img_new
    p0       = p1
    mask     = np.zeros_like( rgb )


# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
