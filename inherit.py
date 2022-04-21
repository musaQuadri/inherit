class Car:
    def __init__(self, modelName, year, price):
        self.modelName=modelName
        self.year=year
        self.price=price

class cab:
    def __init__(self, modelName, year, price, airbag): 
        super.__init__(modelName, year, price)
        self.airbag=airbag

benz=Car('GLK',2021,100000) 
sunny=cab('micra',2010,200000,'null') 


print(benz.__dict__)
print(sunny.__dict__)

