
#----------
# demo of how to use the webcam to capture a brief video
#----------


import numpy as np
import cv2
import time


def VideoCapturer(width,height):
    
    vcap = cv2.VideoCapture(0)
    
    nw0 = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
    nh0 = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    nheight      = 320;
    nwidth       = int(nw0 * nheight / nh0 )
    
    
    vcap.set(cv2.CAP_PROP_FRAME_WIDTH, nwidth)             #set width
    vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, nheight)             #set height
    vcap.set(cv2.CAP_PROP_Frame_NUMBER,100)                       # frame rate

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('brief.avi',fourcc, 20.0, (width,height))

    while(vcap.isOpened()):
        ret, frame = vcap.read()
    #    ret = cap.set(3,320)
    #    ret = cap.set(4,320)
        if ret==True:
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (width,height))
        
            # write the flipped frame
            out.write(frame)
        
            cv2.imshow('working frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    vcap.release()
    out.release()
    cv2.destroyAllWindows()


#----------
# M A I N
#----------



VideoCapturer(640,480)

