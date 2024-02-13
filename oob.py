class Cars:
    def __init__(self, make, model, year):
        self.colour = colour
        self.model = model
        self.make = make
        self.year = year

    def show (self):
        print(f"Selling {self.make} model {self.model} manufactured in {self.year} comes in {self.colour}")
myobj=Cars("Lamboghini","Veneno","2018")
myobj.show()
myobj2=Cars("Nissan","GTR","2014")
myobj2.show()