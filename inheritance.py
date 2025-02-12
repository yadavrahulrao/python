class Person(object):
    def __init__(self, name):
        self.name = name
    def get_details(self):
        return self.name
class Student(Person):
    def __init__(self, name, branch, year):
        super().__init__(name)
        self.branch = branch
        self.year = year
    def get_details(self):
        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)
class Teacher(Person):
    def __init__(self, name, papers):
        super().__init__(name)
        self.papers = papers
    def get_details(self):
        return "%s teaches %s" % (self.name, ','.join(self.papers))
person1 = Person('rahul')
student1 = Student('RAHUL', 'IT', 2027)
teacher1 = Teacher('dimple', ['python'])
print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
