


#----------
# demo of converting webcam frames into hsv images
#----------


import numpy as np
import cv2


def UseWebCam():


    vcap = cv2.VideoCapture(0)

    nw0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    nh0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print nw0, nh0
    
    nheight      = np.uint16(320)
    nwidth       = np.uint16( (nw0/nh0) * nheight  )
    
    print nwidth, nheight

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
    
    
        '''stacking images - vertically'''
        cv2.imshow('HSV space - showing [S]: Press \'q\' to exit >>>',np.vstack((gray,hsv[:,:,2])))
        
        #cv2.imshow('HSV space - showing [V]: Press \'q\' to exit >>>',hsv[:,:,2])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        x = cv2.medianBlur(gray,5)
        cv2.imshow('median blur - To quit, press \'q\'',x)

    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()




#----------
# M A I N
#----------

UseWebCam()



