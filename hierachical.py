#hierachical inheritence
class father():
    def fath(self):
        print(" i am a father")
class child1(father):
    def chil(self):
        print("i am brother")
class child2(father):
    def chill(self):
        print(" i am a child")
f=child1()
f1=child2()
f1.chill()#child2 method
f1.fath()#father method
f.chil()#child1 method
f.fath()#father method


