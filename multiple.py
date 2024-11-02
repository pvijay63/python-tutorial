#multiple inheritence
class father():
    def fath(self):
        print(" iam a father")
class mother():
    def math(self):
        print(" i am a mother")
class child(father,mother):
    def chin(self):
        print(" i am a child")
v=child()
v.chin()#child method
v.math()#mother method
v.fath()#father method
