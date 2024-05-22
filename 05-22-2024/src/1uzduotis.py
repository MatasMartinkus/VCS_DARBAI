##1 užduotis
#	1.1 Apibrėžkite klasę pavadinimu Car.
#	1.2 Klasė turėtų turėti inicializatoriaus metodą, kuris nustato du atributus: markę ir spalvą.
#	1.3 Sukurkite du klasės Car egzempliorius ir išspausdinkite jų atributus.
#	1.4 Į automobilio klasę pridėkite metodą pavadinimu start_engine, kuris spausdina tokį pranešimą kaip "Dabar veikia [markės] [modelio] variklis".
#	1.5 Šį metodą iškvieskite sukurtiems objektams.

class Car:
    def __init__(self, brand:str, model:str) -> None:
        self.brand = brand
        self.model = model

    def start_engine(self) -> str:
        print(f"The engine of {self.brand} {self.model} is on.")

Auto_1 = Car("Mercedes", "G wagon")
Auto_2 = Car("Nissan", "Skyline")

print(Auto_1.brand, Auto_1.model)
print(Auto_2.brand, Auto_2.model)


Auto_1.start_engine()
Auto_2.start_engine()
