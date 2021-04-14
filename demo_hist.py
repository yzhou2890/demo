


#----------
# demo of building histograms for webcam frames
#----------

import numpy as np
import cv2
from matplotlib import pyplot as plt


def UseWebCam():

    vcap = cv2.VideoCapture(0)

    nw0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    nh0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print( 'sensed size:' )
    print( np.uint16(nw0), np.uint16(nh0) )
    
    nheight      = np.uint16(400)
    nwidth       = np.uint16( (nw0/(0.1+nh0)) * nheight  )

    print('reset size:')
    print(nwidth, nheight)

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
            
        img     =  gray
        '''show'''
        cv2.imshow('demo - To quit, press \'q\'', img)

        
        hist,bins = np.histogram( img.flatten(),256,[0,255] )
        cdf = hist.cumsum()
        cdf_normalized = cdf * hist.max()/ cdf.max()

        plt.plot(cdf_normalized, color = 'b')
        plt.hist(img.flatten(),256,[0,256], color = 'r')
        plt.xlim([0,256])
        plt.legend(('cdf','histogram'), loc = 'upper left')
        plt.show()


        if cv2.waitKey(1) & 0xFF == ord('q'):
            plt.close()
            break

    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    UseWebCam()



