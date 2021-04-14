
import numpy as np
import os
import matplotlib.pyplot as plt


np.set_printoptions(precision=15)
'''print 15 digits per num'''

app = Flask(__name__)



@app.route('/')


def hello():
    return 'Hello Heroku!!!'



