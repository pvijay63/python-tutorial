#file handling
'''
reading, writing,deleting, creating of a files is called file handling
open

read/write

close
'''
#file handle modes
'''
r-read
w-write(truncode)
a-append
r+-read write
w+- write read (truncode)
'''
#open and read the txt file
'''a=open('filehand.txt',mode='r')
print(a.read())
a.close()'''
#writing in txt file
'''a=open('filehand.txt',mode='w')
a.write('bye mawa')
a.close()'''
#appending text in txt file without changing it
'''a=open('filehand.txt',mode='a')
a.write('good')
a.close()'''
#read and write in a file
'''
a=open('filehand.txt',mode='r+')
print(a.read())
a.write('r+ nice')
a.read()
a.close()'''
#write and read
'''
a=open('filehand.txt',mode='w+')
a.write("w+ mode")
print(a.read())
a.close()

'''
#write and read output
a=open('filehand.txt',mode='w+')
a.write("w+ mode")
a.seek(0)
print(a.read())




