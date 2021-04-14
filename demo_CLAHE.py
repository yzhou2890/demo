

#----------
# demo of histogram equalization and its variant - CLAHE
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
    
    nwidth      = np.uint16(320*4)
    nheight     = np.uint16( (nh0/nw0) * nwidth  )

    print('reset size:')
    print(nwidth, nheight)

    vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)             #set width
    vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)             #set height
    vcap.set(cv2.CAP_PROP_FPS,20)                       # frame rate

    ret, frame = vcap.read()            # Capture existing frame

    def increase_size(nwidth, nheight):
        if (nwidth < 600):
            nwidth      = np.uint16(nwidth+30)
            nheight     = np.uint16( (nh0/nw0) * nwidth  )            
            return nwidth, nheight
        else:
            return nwidth, nheight


    def increase_size_inv(nwidth, nheight):
        if (nwidth > 50):
            nwidth      = np.uint16(nwidth-30)
            nheight     = np.uint16( (nh0/nw0) * nwidth  )            
            return nwidth, nheight
        else:
            return nwidth, nheight

    print("press q for exit")
    print("press u,i,o for zooming in")
    print("press v,n,m for zooming out")

    print("--------")
    print("top-left:    raw image")
    print("top-right:   histeq only")
    print("bottom-left: CLAHE only")
    print("bottom-right: CLAHE + histeq")

    while(True):
            
        ret, frame = vcap.read()            # Capture frame-by-frame
        # flip left-right
        frame = cv2.flip(frame, 1)
        
        
        '''HSV space'''
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        '''RGB space'''
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        '''gray'''
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
        img     =  cv2.resize(gray, (nwidth, nheight))
        equ     =  cv2.equalizeHist(img)            # histogram equalization

        # create a CLAHE object (Arguments are optional).
        # CLAHE: contrast limited adaptive histogram equalisation
        # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html
        clahe   = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        cl1     = clahe.apply(img)

        equ1    =  cv2.equalizeHist(cl1)            # histogram equalization of CLAHE result

        '''show'''
        cv2.imshow('demo - image enhanced', np.vstack((np.hstack((img, equ)), np.hstack((cl1, equ1)))))
    
        # plt.hist(img.flatten(),256,[0,256], color = 'r')
        # plt.hist(equ.flatten(),256,[0,256], color = 'g')
        # plt.xlim([0,256])
        # plt.legend(('raw','histogram equalized'), loc = 'upper left')
        # plt.show()


        k = cv2.waitKey(1) 
        if k in (ord("q"),ord("p")):
             break

        if k in (ord("u"),ord("i"),ord("o")) :     # increase size
            nwidth, nheight = increase_size( nwidth, nheight )

        if k in (ord("v"),ord("m"),ord("n")) :     # reduce size
            nwidth, nheight = increase_size_inv(nwidth, nheight)

    vcap.release()                  # release the capture if done
    cv2.destroyAllWindows()


#----------
# M A I N
#----------

UseWebCam()
