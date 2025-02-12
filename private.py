class obj:
    __name = None
    __roll = None
    __branch = None
    def __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch
    def __displayDetails(self):
        print("Name:", self.__name)
        print("Roll:", self.__roll)
        print("Branch:", self.__branch)
    def accessPrivateFunction(self):
        self.__displayDetails()
a = obj("Rahul", 23001011049, "Information Technology")
print(a._obj__name)
print(a._obj__roll)
print(a._obj__branch)
a.accessPrivateFunction()

