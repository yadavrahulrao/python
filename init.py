class Student(object):
    def __init__(self, name, branch, year):
            self.name = name
            self.branch = branch
            self.year = year
            print("A student object is created.")
    def print_details(self):
        print("Name:", self.name)
        print("Branch:", self.branch)
        print("Year:", self.year)
a = Student('rahul' , ' it'  ,  ' 2027')
a.print_details()
        
