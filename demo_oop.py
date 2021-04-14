

# object oriented programming + single thread 
# single thread created by user - basic building block for multiple thread system
 
# 1 thread - acquire image from camera and show it

# see demo_multithread.py for a more complete version
# multithread demo
# https://nrsyed.com/2018/07/05/multithreading-with-opencv-python-to-improve-video-processing-performance/


import numpy as np
from threading import Thread
import cv2
from datetime import datetime


class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False

    def start(self):    
        Thread(target=self.get, args=()).start()
        return self

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
                print( self.stream.get(cv2.CAP_PROP_FPS) )

    def stop(self):
        self.stopped = True


def threadVideoGet(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Main thread shows video frames.
    """

    video_getter = VideoGet(source).start()
   
    while True:
        if (cv2.waitKey(1) == ord("q")) or video_getter.stopped:
            video_getter.stop()
            break

        frame = video_getter.frame
        cv2.imshow("Video", frame)



if __name__ == '__main__':
    threadVideoGet()
