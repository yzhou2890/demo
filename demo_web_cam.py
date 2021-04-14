


#----------
# demo of how to use the webcam
#----------


import numpy as np
import cv2


def UseWebCam():

    vcap    = cv2.VideoCapture(0)
    
    nw0     = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
    nh0     = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    nheight      = np.double(360)
    nwidth       = int(nw0 * nheight / nh0 )
    

    vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)             #set width
    vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)           #set height
    
    vcap.set(cv2.CAP_PROP_FPS,10)                       # frame rate

#    vcap.set(cv2.CAP_PROP_EXPOSURE, 0.001)         #set exposure time

    print( nh0, nw0 )
    print(nheight,nwidth)


    while(True):
        # Capture frame-by-frame
        ret, frame = vcap.read()
        # flip left-right
        frame = cv2.flip(frame, 1)

    
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )
    
        # Display the resulting frame
        cv2.imshow('WebCam video: Press \'q\' to exit >>>',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()




#----------
# M A I N
#----------

UseWebCam()



