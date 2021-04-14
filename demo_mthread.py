




# multithread demo
# https://nrsyed.com/2018/07/05/multithreading-with-opencv-python-to-improve-video-processing-performance/

# object-oriented programming + multithread
# 
# 1 thread - acquire image from camera
# 1 thread - to disply raw image
# 1 thread - to calculate Laplacian of Guassian image of the raw image

# see demo_multithread.py for a more complete version - 3 threads with more functions
# see demo_oop.py for a more simplified version - 1 thread only

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

    def stop(self):
        self.stopped = True


# def threadVideoGet(source=0):
#     """
#     Dedicated thread for grabbing video frames with VideoGet object.
#     Main thread shows video frames.
#     """

#     video_getter = VideoGet(source).start()
   
#     while True:
#         if (cv2.waitKey(1) == ord("q")) or video_getter.stopped:
#             video_getter.stop()
#             break

#         frame = video_getter.frame
#         #frame = putIterationsPerSec(frame, cps.countsPerSec())
#         cv2.imshow("Video", frame)
#         #cps.increment()




class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            cv2.imshow("Video", self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True


class VideoShow_edge:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            laplacian = np.array((
                    [0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]), dtype="int")
                                
            x = cv2.filter2D( self.frame, -1, laplacian )

            cv2.imshow("edge",  x)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True


# def threadVideoShow(source=0):
#     """
#     Dedicated thread for showing video frames with VideoShow object.
#     Main thread grabs video frames.
#     """

#     cap = cv2.VideoCapture(source)
#     #(grabbed, frame) = cap.read()
#     video_shower = VideoShow(frame).start()
#     #cps = CountsPerSec().start()

#     while True:
#         (grabbed, frame) = cap.read()
#         if not grabbed or video_shower.stopped:
#             video_shower.stop()
#             break

#         #frame = putIterationsPerSec(frame, cps.countsPerSec())
#         video_shower.frame = frame
#         #cps.increment()





def threadAll(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """

    video_getter = VideoGet(source).start()
    video_shower = VideoShow(video_getter.frame).start()
    video_edgerr = VideoShow_edge(video_getter.frame).start()    # to show image edge online

    while True:
        if video_getter.stopped or video_shower.stopped or video_edgerr.stopped:
            video_shower.stop()
            video_getter.stop()
            video_edgerr.stop()
            break

        frame = video_getter.frame
        video_shower.frame = frame
        video_edgerr.frame = frame
        

        
if __name__ == '__main__':
    threadAll(0)

