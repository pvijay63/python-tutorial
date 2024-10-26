#function
'''
it is a block of code
run when function is called
'''
#ex
def hello():#function definition
    print("a")#body of function
hello()#functin call
#ex1
def sub(a,b):
        print(a-b)
sub(1,8)
#orbitary arguements or parameters
'''
passing multiple arguements to a single parameter
'''
def gio(*a):
    print(a)
gio(2,4,5)

#keyword arguements
'''
passing keyword arguements in a parameter and saves as key ,value pairs in dictionary
'''
def ban(**a):
    print(a)
ban(a=2,b=4,b1=8)


