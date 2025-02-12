class calculation1 () :
        def sum(self,a,b):
                return a+b;
class calculation2 () : 
        def multiply(self , a, b ) : 
                return a*b ;
class derived(calculation1 , calculation2 ): 
        def divide(self, a, b ):
                return a/b;
d= derived()
print(d.sum(10,20))
print(d.multiply(2,3))
print(d.divide(4,2))
