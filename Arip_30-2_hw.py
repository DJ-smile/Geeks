# 1. Создать класс Person с атрибутами fullname, age, is_married
# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks,
#    который был бы словарем, где ключ это название урока, а значение - оценка.
# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
# 6. Добавить в класс Teacher атрибут уровня класса salary
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле:
#    к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
# 9. Написать функцию create_students, в которой создается 3 объекта ученика,
#    эти ученики добавляются в список и список возвращается функцией как результат.
# 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету.
#     Также рассчитать его среднюю оценку по всем предметам.

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"My name is {self.fullname}. I am {self.age} years old.{' I am married.' if self.is_married else ''}")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        num_marks = len(self.marks)
        average_mark = total_marks / num_marks
        return average_mark

class Teacher(Person):
    salary = 20000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05
        return self.salary + (self.salary * bonus)

from modules.teacher import Teacher

# Создаем объект учителя
teacher = Teacher('John Smith', 40, True, 10, 50000)

# Выводим информацию о нем
teacher.introduce_myself()

# Вычисляем его зарплату
salary = teacher.calculate_salary()
print("Зарплата учителя:", salary)

man = Person('Leon', 24, 'no')
print(man)
print(f'name {man.fullname}, age {man.age}, married{man.is_married}')
student_marks = {'Math': 90, 'Science': 85, 'History': 92}
student = Student('Jane Doe', 18, False, student_marks)
print(student.fullname)
print(student.age)
print(student.is_married)
print(student.marks)
print(student.calculate_average_mark())
teacher = Teacher('John Smith', 35, True, 10)
print(teacher.fullname)
print(teacher.age)
print(teacher.is_married)
print(teacher.experience)
Teacher.salary = 25000

teacher1 = Teacher('John Smith', 35, True, 10)
teacher2 = Teacher('Jane Doe', 30, False, 5)

print(teacher1.calculate_salary())
print(teacher2.calculate_salary())