class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def name(self):
        return self.firstname.capitalize()+", "+self.lastname.capitalize()

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        super(Student, self).__init__(firstname, lastname)
        self.subject = subject
    def info(self):
        return self.name()+" studies "+self.subject

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super(Teacher, self).__init__(firstname, lastname)
        self.course = course  
    def info(self):
        return self.name()+" teaches "+self.course