

#----------
# demo of ostu threshold to webcam frames
#----------


import numpy as np
import cv2


def UseWebCam():

    vcap = cv2.VideoCapture(0)

    nw0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    nh0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print('sensed size:')
    print( np.uint16(nw0), np.uint16(nh0) )
    
    nheight      = np.uint16(400)
    nwidth       = np.uint16( (nw0/(0.01+nh0) ) * nheight  )
    
    print('displayed size:')
    print( nwidth, nheight )

    vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)                  #set width
    vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)                #set height
    vcap.set(cv2.CAP_PROP_FPS, 30)                              # frame rate

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
    
    
        ret,th = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)
        
        '''X'''
        X = np.vstack((gray, th))

        cv2.putText(X,'raw image',(3,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1,cv2.LINE_AA)
        cv2.putText(X,'Otsu threshold',(3,nheight+30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(128,0,0),1,cv2.LINE_AA)
        
        '''show'''
        cv2.imshow('Otsu threshold - To quit, press \'q\'', X)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()


#----------
# M A I N
#----------

UseWebCam()
