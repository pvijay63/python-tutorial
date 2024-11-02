#adding string,number 
#error handling
try:
    print('a'+3)
except TypeError:
    print('type error')
except ValueError:
    print('value error')
