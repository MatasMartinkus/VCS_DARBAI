#1 užduotis
#	1.1 Apibrėžkite klasę Animal su atributais name ir species.
class Animal:
    def __init__(self, name:str, species:str) -> None:
        self.name = name
        self.species = species
#	1.2 Pridėkite metodą describe, kuris grąžina eilutę, apibūdinančią gyvūną.
    def describe(self):
        return self.species, self.name
#	1.3 Sukurkite Animal objektą ir iškvieskite metodą describe.

animal1 = Animal("Tom", "Cat")
print(animal1.describe())

