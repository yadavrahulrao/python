# program to understand  local variables 


def change (b) :
        a = 90
        print(a)
a=9          # assigning 9 to a
print(" before the function call " , a)
print("inside change function " , end = ' ' )     
change (a)         # calling  change function
print("after the function call ", a)  # inside that we are assigning 90 to a 

# it actually creating a new variable

