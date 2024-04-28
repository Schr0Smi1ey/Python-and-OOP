class Student:
    def __init__(self,name,cls,id):
        self.name = name
        self.cls = cls
        self.ID = id
    def __repr__(self):
        return f'Student with name : {self.name}, and ID : {self.ID}'


class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.ID = id

    def __repr__(self):
        return f'Teacher : {self.name}, Subject : {self.subject}'
    

class School:
    def __init__(self,name):
        self.name = name
        self.Students = []
        self.Teachers = []
    
    def add_teacher(self,name,subject):
        id = len(self.Teachers) + 1
        self.Teachers.append(Teacher(name,subject,id))
    
    def add_students(self,name,fee):
        id = len(self.Students) + 1
        cls = 3
        if(fee < 6500):
            print(f'Sorry, {name}!! Not sufficient Money.Add more {6500 - fee}.Thank You.')
        else:
            self.Students.append(Student(name,cls,id))
            print(f'Student enrolled with name : {name},id : {id},with extra {6500 - fee}')
    
    def __repr__(self):
        print(f'----------Welcome to {self.name}-----------------')
        print()
        print("-----------Our Teachers Panel--------------")
        for i in self.Teachers:
            print(i)
        print()
        print("-----------Our Student Panel---------------")
        for i in self.Students:
            print(i)
        return f'-------Let\'s begin the mission--------'


phitron = School('Phitron')
phitron.add_students('Sarafat',5000)
phitron.add_students('Karim',6400)
phitron.add_students('Sajjad',6500)
phitron.add_students('Milon',500000)

phitron.add_teacher('Rahat Khan','DS')
phitron.add_teacher('Jhankar','Web Dev')
phitron.add_teacher('Mahbub','Algo')

print(phitron)