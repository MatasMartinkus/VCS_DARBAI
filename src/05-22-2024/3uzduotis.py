# 3 užduotis
#	3.1 Sukurkite Cat klasę.
#	3.2 Pridėkite klasės atributą total_cats, kuris fiksuoja sukurtų katės egzempliorių skaičių.
#	3.3 Inicializatoriuje padidinkite total_cats.
#	3.4 Sukūrę keletą egzempliorių, išspausdinkite bendrą kačių skaičių.

class Cat:
    total_cats = 0
    def __init__(self, name):
        self.name = name
        Cat.total_cats += 1

kate1 = Cat("Mikis")
kate2 = Cat("Tomas")
kate3 = Cat("KateNumeris3")

print(kate3.total_cats)

