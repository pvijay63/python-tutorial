class boy():
    #intialising with init method
    #name and age are public attributes
    def __init__(self,name,age):
        self.boyname=name#public attribute
        self.boyage=age#public attribute
#public member method or function
    def displa(self):
        print(self.boyname)
        print(self.boyage)
b=boy('bik',21)
b.displa()