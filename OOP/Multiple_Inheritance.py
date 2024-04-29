class Identity:
    def __init__(self, Name, Father, Mother, Work):
        self.Name = Name  # Store the student's name
        self.Father = Father  # Store the father's name
        self.Mother = Mother  # Store the mother's name
        self.Work = Work  # Store the student's occupation

    def __repr__(self):
        return f"""
                   My Name is {self.Name},
                   I am a {self.Work},
                   My father name is {self.Father},
                   My mother name is {self.Mother}.
                """  # Return a string representation of the student's identity

class School:
    def __init__(self, cls, ID):
        self.cls = cls  # Store the student's class
        self.ID = ID  # Store the student's ID

    def __repr__(self) -> str:
        return f'I read in class {self.cls} and My student ID is {self.ID}.'  # Return a string representation of the student's school information

class Sports:
    def __init__(self, sport):
        self.sport = sport  # Store the sport played by the student
    
    def __repr__(self) -> str:
        return f'I Play {self.sport} regularly.'  # Return a string representation of the student's sports activity

class Student(Identity, School, Sports):
    def __init__(self, Name, Father, Mother, Work, cls, ID, sport):
        Identity.__init__(self, Name, Father, Mother, Work)  # Initialize the identity of the student
        School.__init__(self, cls, ID)  # Initialize the school information of the student
        Sports.__init__(self, sport)  # Initialize the sports activity of the student

    def __repr__(self):
        return Identity.__repr__(self) + School.__repr__(self) + Sports.__repr__(self)  # Return a string representation of the student

me = Student('John Smith', 'Tim Smith', 'Adriana', 'Student', 6, 201, 'Cricket')
print(me)  # Output the representation of the Student object

# Explanation:
# This code defines three classes: Identity, School, and Sports, representing different aspects of a student's identity.
# The Identity class stores information about the student's name, parents, and occupation.
# The School class stores information about the student's class and student ID.
# The Sports class stores information about the sport the student plays regularly.
# The Student class inherits from Identity, School, and Sports, combining these aspects into a single entity representing a student.
# The __init__ method of the Student class initializes the student's identity, school details, and sports information.
# The __repr__ method of each class provides a string representation of the respective object.
# Finally, an instance of the Student class is created and printed to display the student's information.
