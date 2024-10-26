#dictionary data type
'''
define in curly brackets {}
key,value data(k:v) is called an item
key should be immutable
value should be mutable(different types)
key will out as index
no slicing
keys are unique
'''
#dictionary methods
'''
get()
update()
values()
keys()
items()
'''
a={'name':'vijay','no':90}
print(a['name'])
#get()
print(a.get('no'))
#keys()
print(a.keys())
#values()
print(a.values())
#update()
a.update({'value':4})
print(a)
#using for loop in dictionary
for i in a.values():
    print(i)

for i in a.keys():
    print(i)

for i,j in a.items():
    print(i,j)

for i in a.get('name'):
    print(i)

