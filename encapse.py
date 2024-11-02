#encapsulation

class demo():
    def __init__(self,a,b):
        self.__a=a#private
        self._b=b#protected
class vivo(demo):
    def fet(self):
       print(self._b)
       #print(self._b)#the attributes or variables cant be called in vivo
b=vivo(3,7)
b.fet()
