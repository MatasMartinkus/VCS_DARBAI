import math
#2 užduotis
#	2.1 Apibrėžkite klasę Circle su atributu radius.
class Circle:
    def __init__(self, radius: int) -> None:
        self.radius = radius
#	2.2 Pridėkite metodus area (plotas) ir circumference ("perimetras"), kad apskaičiuotumėte ir grąžintumėte apskritimo plotą ir perimetrą.
    def area(self):
        return math.pi * math.pow(self.radius, 2)
    def perimeter(self):
        return math.pi * 2 * self.radius
#	2.3 Sukurkite apskritimo objektą ir naudokite metodus.
circle = Circle(5)

print(circle.area())
print(circle.perimeter())