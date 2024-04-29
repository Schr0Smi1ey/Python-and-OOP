class Student:
    def __init__(self, name, cls, id):
        self.name = name  # Instance variable storing student's name
        self.cls = cls  # Instance variable storing student's class
        self.ID = id  # Instance variable storing student's ID

    def __repr__(self):
        return f'Student with name: {self.name}, and ID: {self.ID}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name  # Instance variable storing teacher's name
        self.subject = subject  # Instance variable storing teacher's subject
        self.ID = id  # Instance variable storing teacher's ID

    def __repr__(self):
        return f'Teacher: {self.name}, Subject: {self.subject}'


class School:
    def __init__(self, name):
        self.name = name  # Instance variable storing school's name
        self.Students = []  # List to store instances of Student class
        self.Teachers = []  # List to store instances of Teacher class

    def add_teacher(self, name, subject):
        id = len(self.Teachers) + 1  # Generate unique ID for teacher
        self.Teachers.append(Teacher(name, subject, id))  # Create and add Teacher instance to list

    def add_students(self, name, fee):
        id = len(self.Students) + 1  # Generate unique ID for student
        cls = 3  # Set student class
        if fee < 6500:
            # If fee is less than required, print a message
            print(f'Sorry, {name}!! Not sufficient money. Add more {6500 - fee}. Thank you.')
        else:
            # If fee is sufficient, enroll the student and print a message
            self.Students.append(Student(name, cls, id))
            print(f'Student enrolled with name: {name}, ID: {id}, with extra {6500 - fee}')

    def __repr__(self):
        # Method to represent the School object
        # Print school's name and lists of teachers and students
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


# Creating an instance of the School class for 'phitron'
phitron = School('Phitron')

# Adding students and teachers to the school
phitron.add_students('Sarafat', 5000)
phitron.add_students('Karim', 6400)
phitron.add_students('Sajjad', 6500)
phitron.add_students('Milon', 500000)

phitron.add_teacher('Rahat Khan', 'DS')
phitron.add_teacher('Jhankar', 'Web Dev')
phitron.add_teacher('Mahbub', 'Algo')

# Printing information about the school
print(phitron)
