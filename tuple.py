#tuple
'''
allow different type of elements
allow duplicates
allow index and slicing
immutable
no methods we can use builtin
'''
#tuple operations
'''
concatenation
iteration
membership operations
identity operators
repetation
'''
#concatenation
a=(1,2,-2,34,)
b=(2,4)
print(a+b)
#min,max,sum,length operations
print(min(a))
print(max(a))
print(sum(a))
print(len(a))
#repetation
print(b*2)
#iteration
for i in b:
    print(i)
#membership operations
print(2 in b) 
print(5 not in b) 
#identity operators
c1=(1,2)
c2=(2,3)
c3=(1,2)
print(c1 is c3)
print(c1 is not c2)  

