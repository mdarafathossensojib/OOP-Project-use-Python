from classroom import ClassRoom
from school import School
from person import Teacher, Student
from subject import Subject

school = School("ABC School", "Natore")

#Adding ClassRooms
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classRoom(eight)
school.add_classRoom(nine)
school.add_classRoom(ten)

#Adding Student
arafat = Student("Arafat", eight)
jamal = Student("Jamal", eight)
karim = Student("Karim", nine)
rahim = Student("Rahim", ten)
school.student_addmission(arafat)
school.student_addmission(jamal)
school.student_addmission(karim)
school.student_addmission(rahim)

#Adding Teacher
halim = Teacher("Halim")
shamim = Teacher("Shamim")
hannan = Teacher("Hannan")

school.add_teacher("English", halim)
school.add_teacher("Math", shamim)
school.add_teacher("Bangla", shamim)
school.add_teacher("Science", hannan)

#Adding Subject
bangla = Subject("Bangla", shamim)
math = Subject("Math", shamim)
english = Subject("English", halim)
science = Subject("Science", hannan)

eight.add_subject(bangla)
eight.add_subject(math)
eight.add_subject(english)
eight.add_subject(science)
nine.add_subject(bangla)
nine.add_subject(math)
nine.add_subject(english)
ten.add_subject(bangla)
ten.add_subject(math)
ten.add_subject(english)
ten.add_subject(science)

#Semister Final Exam
eight.semister_final_exam()
nine.semister_final_exam()
ten.semister_final_exam()

#Result
print(school)


