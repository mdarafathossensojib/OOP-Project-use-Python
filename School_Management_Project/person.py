import random
from school import School

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def evaluate_exam(self):
        return random.randint(25, 100)

class Student(Person):
    def __init__(self, name, classRoom):
        super().__init__(name)
        self.classRoom = classRoom
        self.__id = None
        self.grade = None
        self.marks = {}
        self.subjects_grade = {}
    
    def final_grade(self):
        sum = 0
        for grade in self.subjects_grade.values():
            point = School.grade_to_value(grade)
            sum += point
        
        if sum == 0:
            gpa = 0
            self.grade = 'F'
        else:
            gpa = sum / len(self.subjects_grade)
            self.grade = School.value_to_grade(gpa)

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id
        
    
