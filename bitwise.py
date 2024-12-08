#bitwiseoperator
'''
comment (~) -- compliment
1s compliement -- 0-1 or 1-0
2s compliment is add 1 to 1s compliment
and (&) --
0 0 -0
1 0 -1
0 1 -1
1 1 -1
or (|)
0 0 -0
1 0 -1
0 1 -1
1 1 -1
xor (^)
0 0 -0
0 1 -1
1 0 -1
1 1 -0

right shift (<<)
convert number into binary 
shift bits  to right according to number
left shift (>>)
convert number into binary 
shift bits  to left according to number

'''
a=2
print(~a)
b=4
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
