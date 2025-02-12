class Student:
    _name = None
    _roll = None
    _branch = None
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch
    def _displayRollAndBranch(self):
        print("Roll:", self._roll)
        print("Branch:", self._branch)
class obj(Student):
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)
    def displayDetails(self):
        print("Name:", self._name)
        self._displayRollAndBranch()
stu = Student("keshav", 2300101105, "Computer Science")
print(stu._name)
stu._displayRollAndBranch()
a= obj("Rahul", 23001011049, "Information Technology")
a.displayDetails()

