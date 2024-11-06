class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Привет, меня зовут {self.fullname}. Мне {self.age} лет. Женат/замужем: {self.is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, base_salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.base_salary = base_salary

    def calculate_salary(self):
        bonus_percentage = max(0, (self.experience - 3) * 0.05)
        total_salary = self.base_salary + (self.base_salary * bonus_percentage)
        return total_salary

def create_students():
    students = []
    student1 = Student("Бактыгуль Аманова", 16, False, {"Математика": 95, "Физика": 87, "История": 78})
    student2 = Student("Сидорова Егина", 17, False, {"Математика": 89, "Физика": 92, "История": 85})
    student3 = Student("Заир Быкытов", 16, False, {"Математика": 78, "Физика": 81, "История": 90})
    students.extend([student1, student2, student3])
    return students

students = create_students()
for student in students:
    student.introduce_myself()
    print("Оценки:")
    for subject, mark in student.marks.items():
        print(f"{subject}: {mark}")
    print(f"Средняя оценка: {student.calculate_average_mark()}")
    print()
teacher = Teacher("Ырыс Жекшенов", 35, True, 7, 50000)
teacher.introduce_myself()
print(f"Опыт работы: {teacher.experience} лет")
print(f"Зарплата: {teacher.calculate_salary()} рублей")
