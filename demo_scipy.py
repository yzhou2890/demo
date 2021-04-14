


from scipy.misc import lena

from matplotlib.pyplot import imshow, gray, show, title

import scipy.ndimage as ndi


image = lena()

imshow(image)
gray()
title('lena from scipy.misc')
show()


sigma = 5
im2 = ndi.filters.gaussian_filter( image, sigma)

imshow(im2)
gray()
title('gaussian blurred')
show()


dx = ndi.filters.sobel(image,0)
dy = ndi.filters.sobel(image,1)

imshow(dx)
gray()
title('gradient - dx')
show()


imshow(dy)
gray()
title('gradient - dy')
show()



import numpy as np

mag = np.sqrt( dx**2 + dy**2 )
ort = np.arctan2(dy,dx)

imshow(mag)
gray()
title('magnitude of gradient')
show()


imshow(ort)
gray()
title('angle of gradient')
show()









