#  program for continue and break statement

while True:
            n = int (input("enter n :"))
            if n < 0 :
                    continue        #this will take the execution back to the starting of the loop
            elif n == 0 :
                    break       # this will get out of loop  
            print(n**2)   #  if n>0 then square of no.  print 
            
print("thanks")            
