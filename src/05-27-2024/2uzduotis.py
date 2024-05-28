#2. Sukurkite bazinę klasę Vehicle su atributais make ir model ir metodu description(), kuris juos atspausdina. 
#Sukurkite išvestinę klasę Car, kuri priima atributą year ir naudoja super(), kad iškviestų bazinės klasės metodą savo aprašymo metode.

class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def description(self):
        print(self.brand, self.model)
    
class Car(Vehicle):
    def __init__(self, brand, model, year) -> None:
        super().__init__(brand, model)
        self.year = year
    
    def description(self):
        super().description()

car = Car("Ferrari", "F40", 1992)
car.description()