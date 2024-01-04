class Besanth:
    discount = 200
    def __init__(self,name):
        self.name=name
        print(name)
        print("hi i am a constructor of class besanth")
    def abc(self):
        discount=100
        print("hi i am from function abc")
        print(self.discount)
        print(discount)
    def xyz(self):
        print(self.discount)
        print(self.name)
obj = Besanth("japan")
obj.abc()
obj.xyz()
