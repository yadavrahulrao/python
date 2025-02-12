with open("sample.txt",'w') as file :
            file.write(" 123 ")

s = input("enter file name : ")
name = open(s)
print(name.read())