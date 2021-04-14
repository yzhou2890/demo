

'''demo of file operations via Python'''


''' open a file to write '''
file = open('test.txt','w')

file.write('abcdefg\n')
file.write('123456\n')
file.write('1')
file.write('1')
file.write('1')
file.write('1')


file.close()



file = open('test.txt','r')

while True:

    line = file.readline()
    if not line: break
    print line


file.close()






