class  parent () : 
        def speak(self) : 
                print(" parents are speaking" )
class child (parent):
        def  walk(self) :
                print("child is walking ") 
class smallchild(child) : 
        def eat (self) : 
                print("small child is eating ")
a = smallchild()
a.speak()
a.walk()
a.eat()
