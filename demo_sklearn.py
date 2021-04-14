
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.set_printoptions(precision=15)

plt.style.use('ggplot')




# http://pandas.pydata.org/pandas-docs/stable/10min.html

#plt.figure()
#plt.ylim((-0.5,1.5))

# public data downloaded from:
#https://factfinder.census.gov/faces/tableservices/jsf/pages/productview.xhtml?pid=ASM_2015_31GS101&prodType=table




# tutorial:
# http://nbviewer.jupyter.org/github/jvns/pandas-cookbook/blob/v0.1/cookbook/Chapter%206%20-%20String%20operations%21%20Which%20month%20was%20the%20snowiest%3F.ipynb







# http://tomaugspurger.github.io/modern-6-visualization.html

# bokeh - python/pandas based visualization for browser

import pandas as pd

df = pd.read_csv('http://vincentarelbundock.github.io/Rdatasets/csv/ggplot2/diamonds.csv');

print df.info()


import bokeh.charts as bc
import bokeh.plotting as bk

fig = (df.assign(xy = df.x / df.y)
       .sample(n=500)
       .pipe(bc.Scatter, 'xy', 'depth'))
bk.show(fig)



# seaborn - for exploratory analysis of statistics
import seaborn as sns
df = sns.load_dataset('titanic')




# factorplot of seaborn
#from sklearn import RandomForestClassifier, GridSearchCV
from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV




logistic = linear_model.LogisticRegression()

pca = decomposition.PCA()
pipe = Pipeline(steps=[('pca', pca), ('logistic', logistic)])

digits = datasets.load_digits()


X_digits = digits.data
y_digits = digits.target

print X_digits.size
print type( X_digits )
print y_digits
print type( y_digits )

pca.fit( X_digits )




plt.figure(1, figsize=(8, 6))
plt.clf()
plt.axes([.2, .2, .7, .7])
plt.plot(pca.explained_variance_ratio_, linewidth=2, marker='*')
plt.axis('tight')
plt.xlabel('n_components')
plt.ylabel('explained_variance_ratio_')

plt.show()




