#1. Sukurkite bazinę klasę Person su atributais name ir age. 
#Apibrėžkite metodą introduce, kuris spausdina pasveikinimą. 
#Sukurkite išvestinę klasę Student, kuri paveldi iš Person ir prideda atributą school_name. Pridėkite metodą print_info(),
#kur atspausdinkite visą žinomą informaciją apie žmogų.

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hello. My name is {self.name}, i am {self.age} years old.")


class Student(Person):
    def __init__(self, name: str, age: int, school_name: str) -> None:
        super().__init__(name, age)
        self.age = age
        self.name = name
        self.school_name = school_name
    
    def print_info(self):
        print(self.name, self.age, self.school_name)

human = Student("Matas", 18, "Vilnius coding school")
human.print_info()