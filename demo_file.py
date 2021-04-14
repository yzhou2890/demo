

'''demo of file operations via Python'''


''' open a file to write '''
file = open('test.xls','w')


''' collect file names for all files within current directory '''
import glob


for filename in glob.glob('*'):    
    file.write( filename + '\n')

for filename in glob.glob('/Volumes/WD_2016/Camelyon16/Data/Train_Tumor/*.tif'):
    file.write( filename + '\n')



file.close()



''' collect python programs and display file names one by one '''
for pyfile in glob.glob('*.py'): 
    print(pyfile)
print('*'*50)



''' use os.listdir  '''
import os

print('$'*50)

for file in os.listdir('.'): 
    print(file)

print('='*50)




