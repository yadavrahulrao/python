# program to open ,read and close the file 

name = input("enter the file name :")  # taking address
f =  open(name)   # opening the file 
a= f.read()
print(a) # reading the file 
f.close()  # closing the file 
