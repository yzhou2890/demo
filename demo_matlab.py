
import numpy as np

import matlab.engine


def product(v1,v2):
    y = 0
    for i in range(0,len(v1)):
        y += v1[i]*v2[i]
    return y/len(v1)




v1 = [0, 1, 1]
v2 = [1, 2, 3]
v3 = np.random.random((700000,1))
v4 = np.random.random((700000,1))


f = product(v1,v2)
print(f)


import matplotlib.pyplot as plt

h = plt.figure('random numbers')
h.patch.set_facecolor('white')
plt.plot(v3[1:20],'ko-')
plt.show()


