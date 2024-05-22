#4 užduotis
#	4.1 Apibrėžkite Rectangle klasę su atributais ilgis ir plotis.
#	4.2 Pridėkite metodus get_area ir get_perimeter, kad apskaičiuotumėte ir grąžintumėte stačiakampio plotą ir perimetrą.
#	4.3 Sukurkite Rectangle objektą ir išspausdinkite plotą bei perimetrą.

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def get_area(self):
        return f"The area of the rectangle is {self.width * self.length}"
    
    def get_perimeter(self):
        return f"The perimeter of the rectangle is {self.width * 2 + self.length * 2}"
    
keturkampis = Rectangle(5, 25)

print(keturkampis.get_perimeter())
print(keturkampis.get_area())