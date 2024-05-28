#3. Sukurkite bazinę klasę Instrument su metodu play, kuris atspausdina pranešimą kad instrumentas groja. Sukurkite 
#dvi išvestines klases Guitar ir Drum, ir taip pat implementuokite metodą play() ir atspausdina info kuris butent instrumentas groja. 
#Parašykite funkciją play_instrument, kuri priima objektą Instrument ir iškviečia jo metodą play.

class Instrument:
    def __init__(self, name) -> None:
        self.name = name

    def play(self):
        print(f"the {self.name} is playing")
    
class Guitar(Instrument):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def play_instrument(self):
        super().play()

class Drums(Instrument):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def play_instrument(self):
        super().play()

        
instrument1 = Guitar("Guitar")
instrument2 = Drums("Drums")

instrument1.play_instrument()
instrument2.play_instrument()        
