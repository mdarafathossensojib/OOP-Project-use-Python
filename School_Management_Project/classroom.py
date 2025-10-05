class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        roll_no = f"{self.name}-{len(self.subjects)+1}"
        student.id = roll_no
        self.students.append(student)
    
    def add_subject(self, subject):
        self.subjects.append(subject)

    def semister_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.final_grade()
            