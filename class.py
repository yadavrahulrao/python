class subject (object):
        def __init__(self,name ,branch,year):
                self.name = name
                self.branch = branch
                self.year = year
                print("a student object is created ")
        def print_details (self): 
                print("name:",self.name)
                print("branch:",self.branch)
                print("year:",self.year)
a = subject('rahul' , 'cse' ,  '2004' )                
a.print_details()
