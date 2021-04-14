# code from: http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/
# import the necessary packages
# from __future__ import print_function
import cv2

# load the image and convert it to grayscale
image = cv2.imread("jurassic_world.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# initialize the AKAZE descriptor, then detect keypoints and extract
# local invariant descriptors from the image
detector = cv2.AKAZE_create()
(kps, descs) = detector.detectAndCompute(gray, None)
print("keypoints: {}, descriptors: {}".format(len(kps), descs.shape))

# draw the keypoints and show the output image
cv2.drawKeypoints(image, kps, image, (0, 0, 255))
cv2.imshow("Output", image)
cv2.waitKey(2000)
