

'''demo of file operations via Python'''


''' open a file to write '''
file = open('test.xls','w')


file.write( 'name\t Y.\t Zhou \n')
file.write('age\t 18\n')
file.write('office\t CM028')

file.close()



file = open('test.xls','r')

while True:

    line = file.readline()
    if not line: break
    
    for x in line.split():
        print x,'\t'

    print '******'

file.close()





