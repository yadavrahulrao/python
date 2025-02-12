# # finding the greatest among the three numbers 


# a = [ 3,4,7]
# b = max(a)
# print(b)



def greatest(a,b,c): 
            if a>b and a>c :
                    return a
            elif b>a and b>c : 
                    return b
            else : 
                    return c 
            
a = int(input("enter a : "))
b = int(input("enter b : "))
c = int (input ("enter c : "))

print("greatest number is : ",greatest(a,b,c))