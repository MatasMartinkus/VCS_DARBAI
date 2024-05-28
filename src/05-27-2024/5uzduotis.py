#5. Parašykite programą, kuri imituotų mokyklos systemą. Implementuokite klases: Person, Teacher, Student, Cource. 
#Programoje turi būti galimybė priskirti studentą prie kurso, atspausdinti informaciją apie kursą: kas dėsto, kiek valandų, koks pažymys.

class Person:
    def __init__(self, name: str, subject: str) -> None:
        self.name = name
        self.subject = subject

class Student(Person):
    def __init__(self, name: str, subject: str, grade: int) -> None:
        super().__init__(name, subject)
        self.grade = grade

class Teacher(Person):
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name, subject)

class Course:
    def __init__(self, students: list, teachers: list, length: int) -> None:
        self.students = students
        self.teachers = teachers
        self.length = length
    
    def add_student(self, student):
        self.students.append(student)
    
    def remove_student(self, student):
        self.students.remove(student)

    def get_subjects(self):
        subject_list = []
        for teacher in self.teachers:
            subject_list.append(teacher.subject)
        return subject_list

    def get_students_by_subject(self, subject):
        students_by_subject_list = []
        for student in self.students:
            if subject == student.subject:
                students_by_subject_list.append(student.name)
        return students_by_subject_list
    
    def get_teachers_by_subject(self, subject):
        teachers_by_subject_list = []
        for teacher in self.teachers:
            if teacher.subject == subject:
                teachers_by_subject_list.append(teacher.name)
        return teachers_by_subject_list
          


    

        

    