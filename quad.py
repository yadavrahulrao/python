# program to evaluate  the roots of quadratic equation . 

import math
a = int(input("enter a :"))
b = int(input("enter b :"))
c = int(input("enter c :"))
d  = b*b - 4 *a * c
if d < 0 :
        print("roots are imaginary")
else :
        r1 =  (-b + math.sqrt(d)) / (2 * a)
        r2 =  ( -b - math.sqrt(d))/(2 * a )
        print( r1)
        print (r2)
