class grandfather():
    def genius(self):
        print("i am a grandfather")
class parent(grandfather):
    def gen(self):
        print("i am a parent")
class child(parent):
    def present(self):
        print("i am a child")
big=child()
big.present()
big.gen()
big.genius()