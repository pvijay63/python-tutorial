a=8#global variable or static variable
def a1():
    c=5#local variable or instance variable
    print(a)
    print(c)
a1()

#converting local variable into global
u=8
def t():
    y=7
    global y1
    y1=7
    print(u)
t()
print(y1)    

