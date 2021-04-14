


#----------
# demo of converting webcam frames into blurred images (via median filtering)
#----------


import numpy as np
import cv2


def UseWebCam():


    vcap = cv2.VideoCapture(0)

    nw0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    nh0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print( nw0, nh0 )
    
    nheight      = np.uint16(400)
    nwidth       = np.uint16( (nw0/nh0) * nheight  )
    
    print( nwidth, nheight )

    vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)             #set width
    vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)             #set height
    
    
    vcap.set(cv2.CAP_PROP_FPS,10)                       # frame rate

#    vcap.set(cv2.CAP_PROP_EXPOSURE, 0.001)         #set exposure time



    while(True):
        # Capture frame-by-frame
        ret, frame = vcap.read()
        # flip left-right
        frame = cv2.flip(frame, 1)
        
        
        '''HSV space'''
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        '''RGB space'''
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        '''gray'''
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    
        '''median filtering'''
        r = cv2.medianBlur( rgb[:,:,0], 9)
        g = cv2.medianBlur( rgb[:,:,1], 9)
        b = cv2.medianBlur( rgb[:,:,2], 9)
        
        '''X'''
        X = np.vstack((rgb,cv2.merge((r,g,b))));
        cv2.putText(X,'raw image',(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1,cv2.LINE_AA)
        cv2.putText(X,'blurred image',(10,nheight+30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1,cv2.LINE_AA)

        '''show'''
        cv2.imshow('median blur - To quit, press \'q\'', X)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()




#----------
# M A I N
#----------

UseWebCam()



