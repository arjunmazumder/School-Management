from school import School
from person import Teacher,Student
from subjects import Subject
from classroom import ClassRoom
#School banailam
school = School(name="KPA",address="Dhaka")
#ClassRoom banailam three ta
ClassEight = ClassRoom(name="Eight")
ClassNine = ClassRoom(name="Nine")
ClassTen = ClassRoom(name="Ten")
#ClassRoom school e add korlam
school.add_classroom(classRoom=ClassEight)
school.add_classroom(classRoom=ClassNine)
school.add_classroom(classRoom=ClassTen)

#Student banalam four ta
arjun = Student(name="Arjun",classroom="Eight")
nilu = Student(name="Nilu",classroom="Ten")
tasfia = Student(name="Tasfia",classroom="Ten")
mitu = Student(name="Mitu",classroom="Eight")
rupa = Student(name="Rupa",classroom="Nine")
shahin = Student(name="Shahin",classroom="Nine")

#student add korlam school e 
school.student_admission(arjun)
school.student_admission(nilu)
school.student_admission(tasfia)
school.student_admission(mitu)
school.student_admission(rupa)
school.student_admission(shahin)
#Teacher banalam 
babul = Teacher(name="Buble")
parimal = Teacher(name="Parimal")
amrito = Teacher(name="Amrito")
nitto = Teacher(name="Nitto")
#subject banalam
bag = Subject(name="Bangla",teacher=babul) 
eng = Subject(name="English",teacher=parimal) 
math = Subject(name="Math",teacher=amrito) 
sce = Subject(name="Science",teacher=nitto) 
#subject add korbo class eight er jonno
ClassEight.add_subject(bag)
ClassEight.add_subject(eng)
ClassEight.add_subject(math)
#subject add korbo class nine er jonno
ClassNine.add_subject(math)
ClassNine.add_subject(eng)
ClassNine.add_subject(sce)
#subject add korbo class Ten er jonno
ClassTen.add_subject(sce)
ClassTen.add_subject(bag)
ClassTen.add_subject(math)

ClassEight.take_semester_final_exam()
ClassNine.take_semester_final_exam()
ClassTen.take_semester_final_exam()
print(school)





