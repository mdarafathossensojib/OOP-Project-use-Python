class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # {subject: Teacher(object)}
        self.classRooms = {} # {Class Name : ClassRoom(object)}

    def add_classRoom(self, classRoom):
        self.classRooms[classRoom.name] = classRoom
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    def student_addmission(self, student):
        classname = student.classRoom.name
        self.classRooms[classname].add_student(student)

    @staticmethod
    def claculate_grade(marks):
        if marks >= 80:
            return 'A+'
        elif marks >= 70:
            return 'A'
        elif marks >= 60:
            return 'A-'
        elif marks >= 50:
            return 'B'
        elif marks >= 40:
            return 'C'
        elif marks >= 33:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_value = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00
        }
        return grade_value[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value == 5.00:
            return 'A+'
        elif value >= 4.00:
            return 'A'
        elif value >= 3.50:
            return 'A-'
        elif value >= 3.00:
            return 'B'
        elif value >= 2.00:
            return 'C'
        elif value >= 1.00:
            return 'D'
        else:
            return 'F'
        
    def __repr__(self):
        #All ClassRooms
        for key in self.classRooms.keys():
            print(key)
        #All Students
        print("All Students List")
        result = ''
        for key, value in self.classRooms.items():
            result += f"---{key.upper()} ClassRoom Students---\n"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)
        #All Teachers
        print("All Teachers List")
        result = ''
        for subject, teacher in self.teachers.items():
            result += f"{subject} : {teacher.name}\n"
        print(result)
        #All Subjects
        print("All Subjects List")
        subject = ''
        for key, value in self.classRooms.items():
            subject += f'---{key.upper()} ClassRoom Subjects---\n'
            for sub in value.subjects:
                subject += f'{sub.name}\n'
        print(subject)
        #All Students Result
        print("All Students Result")
        for key, value in self.classRooms.items():
            for student in value.students:
                for k, i in student.marks.items():
                    print(f"{student.name} got {i} in {k} grade {student.subjects_grade[k]}")
                print(f"Final Grade: {student.final_grade()}\n")
        
        return ''
