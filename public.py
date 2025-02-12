class  obj:
    def __init__(self, name, age):
        self.objName = name
        self.objAge = age
    def displayAge(self):
        print("Age: ", self.objAge)
a = obj("Rahul", 20)
print("Name:", a.objName)
a.displayAge()

