class Fruits:
    def __init__(self,Type,Price):
        self.Type=Type
        self.Price=Price
    def show(self):
     print(f"my favourite fruit is {self.Type} and it costs ksh.{self.Price}")
myobj=Fruits("Mangoes","150")
myobj.show()
myobj1=Fruits("Apples","200")
myobj1.show()
myobj2=Fruits("Pineapples","450")
myobj2.show()
myobj3=Fruits("Grapes","1000")
myobj3.show()
myobj4=Fruits("Melons","800")
myobj4.show()


