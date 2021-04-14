
import matplotlib.pyplot as plt

import numpy as np

from numpy.random import normal


a = np.linspace(0, 10, 100)

b = np.exp(-a)

if False==True:
    plt.plot(a,b)
    plt.show()


x = normal(size=200)

h = plt.figure()
h.patch.set_facecolor('white')

plt.hist(x,bins=30)
plt.xlabel('bins')
plt.ylabel('counts')
plt.show('histogram')



