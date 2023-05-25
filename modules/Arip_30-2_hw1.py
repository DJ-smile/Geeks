class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"My name is {self.fullname}, I'm {self.age} years old.")
        if self.is_married:
            print("I'm married.")
        else:
            print("I'm not married.")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def get_average_mark(self):
        marks_sum = 0
        for mark in self.marks.values():
            marks_sum += mark
        return marks_sum / len(self.marks)


class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = 1000 + self.experience * 50 if self.experience > 3 else 1000

    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05
        return self.salary + self.salary * bonus


def create_students():
    students = []
    student1 = Student("John Doe", 17, False, {"Math": 5, "Literature": 4, "History": 3})
    student2 = Student("Jane Smith", 16, False, {"Math": 4, "Literature": 5, "History": 4})
    student3 = Student("Bob Johnson", 18, False, {"Math": 3, "Literature": 3, "History": 5})
    students.append(student1)
    students.append(student2)
    students.append(student3)
    return students


if __name__ == '__main__':
    teacher = Teacher("Alice Brown", 35, True, 7)
    teacher.introduce_myself()
    print(f"My salary is {teacher.calculate_salary()} dollars.")

    students = create_students()
    for student in students:
        student.introduce_myself()
        for subject, mark in student.marks.items():
            print(f"{subject}: {mark}")
        print(f"Average mark: {student.get_average_mark()}")
