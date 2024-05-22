#5 užduotis
#	5.1 Apibrėžkite klasę pavadinimu Student.
#	5.2 Klasė turi turėti inicializatorių, kuris nustato du atributus: name, class ir grade.
#	5.3 Pridėkite metodą get_grade, kad grąžintumėte įvertinimą.
#	5.4 Pridėkite metodą set_grade, kad pakeistumėte įvertinimą (užtikrinkite, kad įvertinimas būtų nuo 0 iki 100).
#	5.5 Pridėkite metodą print_studen_info, kuris gražintų informaciją apie studentą.
#	5.6 Sukurkite egzempliorių ir išbandykite metodus.

class Student:
    def __init__(self, name:str, grade:int) -> None:
        self.name = name
        self.grade = grade

    def get_grade(self) -> str:
        return f"The grade of {self.name} is {self.grade}"
    
    def set_grade(self, new_grade: int):
        if new_grade in range(0, 101):
            self.grade = new_grade
        else:
            print(f"Bad input")

    def print_student_info(self) -> str:
        return f"Student name: {self.name}\nStudent grade: {self.grade}"
    
student1 = Student("Rudolfas", 78)
print(student1.get_grade())
student1.set_grade(25)
print(student1.get_grade())
student1.set_grade(105)
