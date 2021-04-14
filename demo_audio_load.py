


# load an audio file into the workspace of python


import numpy as np
from scipy.io.wavfile import read



[rate, data] = read( 'test.mp3' )


# show data as a curve
import matplotlib.pyplot as plt

plt.figure(facecolor='w')
plt.plot( data[0:min(1000,np.size(data))])
plt.xlabel('time')
plt.ylabel('value')
plt.legend(['test.mp3'])
plt.show()




# play data via speaker

import pyglet
song    = pyglet.media.audiodata(rate,data)
song.play()



# use pyglet package
import pyglet
song = pyglet.media.load('test.mp3')
song.play()

