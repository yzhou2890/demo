


#--------------------------------------
# demo of subsampling via cv2.pyrDown()
#--------------------------------------


import numpy as np
import cv2


def UseWebCam():

    vcap = cv2.VideoCapture(0)

    nw0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    nh0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print nw0, nh0
    
    nheight      = np.uint16(400)
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
        
    
        '''Gaussian filtering'''
        r = cv2.GaussianBlur( rgb[:,:,0], (19,19),0)
        r = cv2.pyrDown(r)
        g = cv2.GaussianBlur( rgb[:,:,1], (19,19),0)
        g = cv2.pyrDown(g)
        b = cv2.GaussianBlur( rgb[:,:,2], (19,19),0)
        b = cv2.pyrDown(b)


        '''X'''
        X = cv2.merge((r,g,b))
        cv2.putText(X,'subsampled image',(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1,cv2.LINE_AA)


        '''show'''
        cv2.imshow('original', rgb)
        cv2.imshow('subsampled', X)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print rgb.shape, X.shape
            break


    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':

    UseWebCam()



