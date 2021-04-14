
# demo - opencv
 

import cv2
 
# Black and White (gray scale)
 
img = cv2.imread ('lotus.jpg', 1 )
 
cv2.imshow('lotus', img)
 
cv2.waitKey(0)
 
# cv2.waitKey(2000)
 
cv2.destroyAllWindows()


