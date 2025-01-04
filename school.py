# from classroom import ClassRoom

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} #{SubjectName : teacher Object}
        self.classRooms = {} #{ClassRoom : ClassRoom Object}
    
    def add_classroom(self, classRoom):
        self.classRooms[classRoom.name]=classRoom
    def add_teacher(self, subject, teacher):
        self.teachers[subject]=teacher

    def student_admission(self, student):
        className = student.classroom
        self.classRooms[className].add_student(student)
      
    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks<=100:
            return 'A+'
        elif marks >= 70 and marks < 80:
            return 'A'
        elif marks >=60 and marks < 70:
            return 'A-'
        elif marks >= 50 and marks <60:
            return 'B'
        elif marks >= 40 and marks <50:
            return 'C'
        elif marks >=33 and marks <40:
            return 'D'
        else:
            return 'F'
    @staticmethod
    def grad_to_point(grade):
        grad_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grad_map[grade]
    
    @staticmethod
    def total_point_to_grad(totalPoint):
        if totalPoint >= 4.5 and totalPoint <= 5.00:
            return 'A+'
        elif totalPoint >= 4.00 and totalPoint < 4.50 :
            return 'A'
        elif totalPoint >= 3.50 and totalPoint < 4.00 :
            return 'A-'
        elif totalPoint >= 3.00 and totalPoint < 3.50:
            return 'B'
        elif totalPoint >=2.50 and totalPoint < 3.00:
            return 'C'
        elif totalPoint >= 2.00 and totalPoint <2.50:
            return 'D'
        else:
            return 'F'
    def __repr__(self):
        # all classroom 
        for key in self.classRooms.keys():
            print(key)
        
        # all student
        print("All Students")
        result = ''
        for key, value in self.classRooms.items():
            result += f"---{key.upper()} classroom Student\n"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)
        # all subject
        subject = ''
        for key, value in self.classRooms.items():
            subject += f"---{key.upper()} classroom subject\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)
        # all teacher
        # all result
        print("All Students Results")
        for key, value in self.classRooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grad[k])
                print(student.final_grade())

        return ''
       



    
