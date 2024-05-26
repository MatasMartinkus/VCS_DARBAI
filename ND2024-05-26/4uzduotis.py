#4 užduotis
#	4.1 Apibrėžkite klasę Teacher su atributais name ir subject.
class Teacher:
    def __init__(self, name, subject) -> None:
        self.name = name
        self.name = subject
#	4.2 Apibrėžkite klasę Klasė su atributais mokytojas (Mokytojo egzempliorius) ir mokiniai (mokinių vardų sąrašas).
class Class:
    def __init__(self, teacher, students: list) -> None:
        self.teacher = teacher
        self.students= students
#	4.3 Į klasę Classroom įtraukite metodus, skirtus mokiniui pridėti ir mokiniui pašalinti.
    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)
    
#	4.4 Sukurkite Mokytojo ir Klasės objektus, pridėkite ir pašalinkite mokinius iš klasės.

teacher1 = Teacher("Barbora", "Physics")
clasroom = Class(teacher1, ["Matas", "Brigita", "Saulius"])
print(clasroom.students)
clasroom.add_student("Irma")
print(clasroom.students)
clasroom.remove_student("Matas")
print(clasroom.students)
