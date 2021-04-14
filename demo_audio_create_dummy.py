

# demo - create a dummy audio file and save it

import numpy as np
from scipy.io.wavfile import write

rate = 44100
sec  = 5
data = np.random.uniform( 0, 1, rate*sec)
sig  = np.int16( data * 32767 )

write('Music/test.mp3',rate, sig)









