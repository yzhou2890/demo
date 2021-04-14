

# demo of how to use the webcam

import numpy as np
import cv2

def UseWebCam():

    vcap        = cv2.VideoCapture(0)
    nheight     = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
    nwidth      = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)              #set width
    vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)            #set height    
    vcap.set(cv2.CAP_PROP_FPS,25)                           # frame rate
#    vcap.set(cv2.CAP_PROP_EXPOSURE, -3.5 )                  #set exposure parameter - gamma ?

    print(nheight,nwidth)
    print( vcap.get(cv2.CAP_PROP_FPS) )
    print("press s to save current frame")

    while(True):
        # Capture frame-by-frame
        ret, frame = vcap.read()
        # flip left-right
        frame = cv2.flip(frame, 1)

        # Our operations on the frame come here
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY )
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB )
    
        # Display the resulting frame
        cv2.imshow('demo: \'s\' to save, \'q\' to exit >>>', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite( "tmp.jpg", frame)
            print("Image saved as tmp.jpg")
            
            

    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()

UseWebCam()



