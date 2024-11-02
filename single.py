class parent():
    def good(self):
        print("i am a parent")
class child(parent):
    def china(self):
        print("i am  a child")
c=child()
c.china()#child method 
c.good()#parent method

