
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


np.set_printoptions(precision=15)


# http://pandas.pydata.org/pandas-docs/stable/10min.html


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))


plt.figure()
ts.plot(label='raw data')
ts = ts.cumsum()
ts.plot(label='cumulative data')

plt.show()

print len(ts)


data = pd.Series(np.random.randn(1000))

data.hist(by=np.random.randint(0, 10, 1000), figsize=(10, 10))
plt.show()



'''



df_1D = pd.DataFrame( np.random.randn(10000,1) )
df_1D.plot.hist()



s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20130101', periods=6)

# print dates


df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df

print df.A
print df['B']

print df.loc[:,['A','B']]
print df.iloc[0:2,1:3]
print df.iat[1,1]

print df[df.A>0]



print df.head(2)

print df.tail(2)


print df.index
print df.columns

np.set_printoptions(precision=5)
print df.values
np.set_printoptions(precision=15)

print df.T
print df.sort_values(by='B',ascending= False )

print pd.isnull( df )


print df.mean()

def func(v3):
    h = plt.figure('random numbers')
    h.patch.set_facecolor('white')
    plt.plot(v3[1:20],'ko-')
    plt.ylim((-0.5,1.5))
    plt.show()




df2 = pd.DataFrame({ 'A' : 1.,
                   'B' : pd.Timestamp('20130102'),
                   'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                   'D' : np.array([3] * 4,dtype='int32'),
                   'E' : pd.Categorical(["test","train","test","train"]),
                   'F' : 'foo' })

print df2

print df2.dtypes






# pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
# df.to_excel('foo.xlsx', sheet_name='Sheet1')
# 
#


#
xlsx = pd.ExcelFile('path_to_file.xlsx' )
                    
#df = pd.read_excel(xlsx, 'Sheet1')
                    
# df.to_excel('foo.xlsx', sheet_name='Sheet1')

df.to_excel( xlsx, sheet_name='Sheet1')






# df = pd.read_excel('JSTdatasetR2.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
df = pd.read_excel('JSTdatasetR2.xlsx')

df.head(10)

'''



