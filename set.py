#set datatype
'''
defined in curly brackets {}
do not allow duplicates
no index,unordered
do not allow mutable types as set elements
'''
#set methods
'''
add()
update()
pop()
remove()
'''
#set opertions
'''
union()
interjunction()
difference()
issubset()
issuperset()
'''
a={2,4,-1,0,2}
print(a)
#add()
a.add(4)
print(a)
#update()
a.update({3,5,6,7,8})
print(a)
#pop()
a.pop()
print(a)
#remove
a.remove(4)
print(a)
#set operations
s1={1,23,3}
s2={3,2,4}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

c1={0,1}
c2={0,1,2,3}
print(c1.issubset(c2))
print(c2.issuperset(c1))

#using for loop in set
for i in {2,3,4}:
    print(i)
