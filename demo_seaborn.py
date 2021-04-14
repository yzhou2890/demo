
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



# matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(x='carat', y='depth', data=df, c='k', alpha=.15)
plt.show()




# pandas built-in plot
df.plot.scatter(x='carat', y='depth', c='k', alpha=.15)

from pandas_datareader import fred

gdp = fred.FredReader(['GCEC96', 'GPDIC96'], start='2000-01-01').read()
gdp.rename(columns={"GCEC96": "Government Expenditure",
           "GPDIC96": "Private Investment"}).plot(figsize=(12, 6))

plt.show()



# seaborn - for exploratory analysis of statistics
import seaborn as sns

sns.countplot(x='cut', data=df)
sns.despine()
plt.show()

sns.barplot(x='cut', y='price', data=df)
sns.despine()
plt.show()


sns.jointplot(x='carat', y='price', data=df, size=8, alpha=.25,
              color='k', marker='.')
plt.show()

# seaborn - very useful for exploratory study but time-consuming
import seaborn as sns
#g = sns.pairplot(df, hue='cut')
#plt.show()



# facetgrid of seaborn
import seaborn as sns
g = sns.FacetGrid(df, col='color', hue='color', col_wrap=4)
g.map(sns.regplot, 'carat', 'price')

plt.show()



# cubehelix of seaborn
import seaborn as sns

df = df.iloc[:,1:7]

def core(df, alpha =.05):
    mask = (df > df.quantile(alpha)).all(1) & ( df < df.quantile(1 - alpha)).all(1)
    return df[mask]

cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)

(df.select_dtypes(include=[np.number])
 .pipe(core)
 .pipe(sns.PairGrid)
 .map_upper(plt.scatter, marker='.', alpha=.25)
 .map_diag(sns.kdeplot)
 .map_lower(plt.hexbin, cmap=cmap, gridsize=20)
 )
plt.show()




# factorplot of seaborn
from sklearn import RandomForestClassifier, GridSearchCV
from sklearn import linear_model, decomposition, datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

df = sns.load_dataset('titanic')

clf = RandomForestClassifier()
param_grid = dict(max_depth=[1, 2, 5, 10, 20, 30, 40],
                  min_samples_split=[2, 5, 10],
                  min_samples_leaf=[2, 3, 5])
est = GridSearchCV(clf, param_grid=param_grid, n_jobs=4)

y = df['survived']
X = df.drop(['survived', 'who', 'alive'], axis=1)

X = pd.get_dummies(X, drop_first=True)
X = X.fillna(value=X.median())
est.fit(X, y)


scores = est.grid_scores_
rows = []
params = sorted(scores[0].parameters)
for row in scores:
    mean = row.mean_validation_score
    std = row.cv_validation_scores.std()
    rows.append([mean, std] + [row.parameters[k] for k in params])
scores = pd.DataFrame(rows, columns=['mean_', 'std_'] + params)

sns.factorplot(x='max_depth', y='mean_', data=scores, col='min_samples_split',
               hue='min_samples_leaf')



