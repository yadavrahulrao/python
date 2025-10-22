#Tuple
#tuple are used to store multiple items in a single variable.

#tuples are ordered , unchangeable , or allow duplicates

# a = ("afsjvbsdj" , "ddlshfi" , "fkajhfiu")
# print(a)

# a = ("adasf",)
# print(a)


# a = (100,24, 23423,23,325)
# print(a[2:5])

# tuples are unchangeable , so first we can change a tuple into a list then we remove , add , change 
# the list . after that we can convert the list into a tuple

# a = ("rao" ,"kill")
# y = list(a)
# y[0] = "go"
# a = tuple(y)
# print(a)


# we can also add a tuple into a tuple .

# we can also use del keyword for deleting a tuple

# a = ( " apple ", "cheery")
# y = list(a)
# y.append("hello")
# a = tuple(y)
# print(a)


# we can we remove keyword to remove a item from the tuple

 # if we assign the value to a tuple then this is the packing of a tuple 

# a = ("rahul","rao","yadav")
# (red, green, black)  = a
# print(red)


# a = ("rao", "rahul","yadav")
# for x in a :
#   print(x)

# a = ("har","ahr","sjd")
# i = 0
# while i< len(a):
#   print(a[i])
#   i += 1


# we can add two tuple using +operator  or multiply them

# a = (23,34,45)
# b = (3,4,6)

# c = a + b
# print(c)

# a = ("rafm" , "dfkjf")

# b = a*2
# print(b)

names = ["Nitesh","Ravi" , "Aman"]
for n in names:
  print(n[0])