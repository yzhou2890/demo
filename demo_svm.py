
# demo of using svm to classify 2D cloud points


import cv2

import numpy as np


x1 = np.random.randint(  1, 100, [50, 2] )
x2 = np.random.randint(105, 200, [50, 2] )
trainData = np.vstack( (x1, x2))

y1 = np.zeros(50)
y2 = np.ones(50)
responses = np.hstack((y1,y2)).transpose()

for x, y in zip(trainData,responses)
    print x,y

svm_params = dict( kernel_type = cv2.SVM_LINEAR,
                   svm_type = cv2.SVM_C_SVC,
                   C = 2.67, gamma = 5.383 )

svm = cv2.SVM()

svm.train(trainData, responses, params=svm_params)



