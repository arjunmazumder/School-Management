import random
from school import School


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        
    def evaluate_exam(self):
        return random.randint(60,100)

class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {} #{bang : 78}
        self.subject_grad = {} #{bang : A}
        self.grade = None

    def final_grade(self):
        sum = 0
        for grade in self.subject_grad.values():
            point = School.grad_to_point(grade)
            sum += point
        gpa = sum/(len(self.subject_grad)+1)
        self.grade = School.total_point_to_grad(gpa)
        return f"{self.name} Final Grade : {self.grade} with GPA = {gpa}"

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value




        