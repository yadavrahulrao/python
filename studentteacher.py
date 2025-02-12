class person(object)
        def __init__(self,name)
                self.name = name
        def get_details(self)
                return self.name
class student (person)
        def __init__(self,name,branch,year)
                person.__init__(self,name)
                
        
