





#--------------------------------
# demo of convolution of 2D image - laplacian kernel 
#--------------------------------


import numpy as np
import cv2


def UseWebCam():


    vcap = cv2.VideoCapture(0)

    nw0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    nh0 = np.float(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print(nw0, nh0)
    
    nheight      = np.uint16(400)
    nwidth       = np.uint16( (nw0/nh0) * nheight  )
    
    print(nwidth, nheight)

    vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)             #set width
    vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)             #set height
    
    
    vcap.set(cv2.CAP_PROP_FPS,20)                       # frame rate

#    vcap.set(cv2.CAP_PROP_EXPOSURE, 0.001)         #set exposure time


    kernel = np.ones( (9,9), np.float32 )/81

    # laplacian kernel
    laplacian = np.array((
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]), dtype="int")

    # construct the Sobel x-axis kernel
    sobelX = np.array((
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]), dtype="int")

    # construct the Sobel y-axis kernel
    sobelY = np.array((
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]), dtype="int")

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
        
        '''processing'''
        kernel = laplacian              # sobelY  #
        x = cv2.filter2D( gray, -1, kernel )
        X = np.vstack((gray, x))
        

        cv2.putText(X,'raw image',(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1,cv2.LINE_AA)
        cv2.putText(X, 'image processed',(10,nheight+30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1,cv2.LINE_AA)

        '''show'''
        cv2.imshow('img and its processing - To quit, press \'q\'', X)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':

    UseWebCam()











