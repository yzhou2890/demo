
'''
    display two trackbars on the image
    toggle trackbars to change the destination of the line-arrow on the image (constant valued)
    '''


import numpy as np
import cv2



def nothing(x):
    pass


img = np.ones((300,300,3),np.uint8)*200

str =  'demo of gui'
cv2.namedWindow(str)

cv2.createTrackbar('theta',str,1,89,nothing)
cv2.createTrackbar('rho',str,10,400,nothing)

while (1):
    cv2.imshow(str,img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        print(theta,rho)
        break

    theta = cv2.getTrackbarPos('theta',str)*np.pi/180
    rho = cv2.getTrackbarPos('rho',str)



    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'opencv',(10,200),font,2,(0,255,0),1, cv2.LINE_AA)

    cv2.arrowedLine(img,(0,0),(int(np.cos(theta)*rho),int(np.sin(theta)*rho)),(255,0,0),2)

    if theta < 0.1:
        img[:] = np.random.random(1)*300+300

cv2.destroyAllWindows()
