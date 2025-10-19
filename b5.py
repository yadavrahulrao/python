# import time 
# for i in range(10,0,-1):
#   print(i,end="\r",flush=True)
#   time.sleep(1)
# print("Go!")


# a = ["rahul" , " rohit" , "varun"]
# a[1] = "rao"
# print(a)

# a = ["apple" , "banana", " cherry"]
# a[1:2] = ("kiwi","mango")
# print(a[2])

# if we use append then we have to only append list
# if we extend list then we have to add iterable values(list , tuple , dictionary, sets)


# a = ["apple" , "banana" , "chherry"]
# a.insert(0,"orange")
# print(a[1])

# in list remove can remove a specific element
# pop is used for a specific index
#del is for specific index or the entire list

# clear is for empities the entire list

a = [1,2,4]

# for x in a:
#   print(x)

# for i in range (len(a)):
#   print(a[i])

# i = 0
# while i < len(a):
#   print(a[i])
#   i += 1

# [print(x) for x in a]

# list comprehension is for crating a ne list from the exixting list

a = ["abc" ,"bcd", "akjhdsf","ksdgf"]

# b = []
# for i in a :
#   if "a" in i:
#     b.append(i)
# print(b)


# b = [x for x in a if "a" in x]
# print(b)


# a = ["apple" ,"banana" , "cherry"]

# a.sort()
# n = ["apple" for x in a ]
# print(a)

# using sort()  is a case insensitive sort .

# x = [100,20,30,10,40,80]
# x.sort()
# x.sort(reverse=True)

# x.reverse()

# print(x)


# def fun(n):
#   return abs(n - 50)

# a = [100,30,20,50,40,10]
# a.sort(key=fun)
# print(a)

# we can use copy(), list. , or slicing for copy of one list to another

# a = [20 , 10 , 33 , 44]
# x = a.copy()
# print(x)

# x = list(a)
# print(x)

# x = a[:]
# print(x)


# we can join two lists using +operator , using append and extend.

# l1 = [23,34,45,56]
# l2 = [23,324,345,456]
# print(l1+l2)


# l1 = ["rao"]
# l2 = [34]
# for x in l2:
#   l1.append(x)
# print(l1)


# l1 = [324]
# l2 = ["rahul"]
# l1.extend(l2)
# print(l1)


