


import numpy as np
from threading import Thread
import cv2


img = cv2.imread("lotus.jpg", cv2.IMREAD_COLOR)

src = cv2.cuda_GpuMat()
src.upload(img)

clahe = cv2.cuda.createContinuous()

dst = clahe.apply(src, cv2.cuda_Stream.Null())

result = dst.download()

cv2.imshow("result", result)

cv2.waitKey(0)






