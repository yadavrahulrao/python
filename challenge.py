# class A:
#   data = []
# a = A()
# b = A()
# a.data.append(5)
# print(b.data)

# for i in range(1,10,3):
#   print(i)
#   if(i==4):
#     break


# for i in range(3):
#   print(i)

# else :
#   print("code loop completed without break")


# 5 + 7
# _ + 3


# name = ["rahul","rohit"]
# age = [20,22]
# for n,a in zip(name,age):
#   print(f"name is {n},age is {a}")


# eq = '130 + 132 = 262'
# for i in eq:
#   if i not in '11':
#     print(i)


# class shape :
#   def area(self):
#     return 0
# class circle(shape):
#   def __init__(self,radius):
#     self.radius = radius
#   def area(self):
#     return 3.14 * self.radius * self.radius

# c = circle(2)
# r = c.area()
# print(r)


# n = [1,2,3,4,5]
# t = 0
# for i in n :
#   t += i
# print(t)


# t= (1,2,3,4)
# t= (1,2,3,4)
# r = t +(5,)
# print(r)
# r = t +(5,)
# print(r)

# def power(x,n):
#   return x**n
# r = power(2,3)
# print(r)


# x = [1,2,3]
# print(x[::-1])



# class A:
#   def __getattribute__(self,name):
#     if name == "x":
#       return 10
#     return super().__getattribute__(name)
#   def __getattr__(self,name):
#     return 20
# a = A()
# print(a.x , a.y)


# for i in range(3):
#   print(i)

# else:
#   print("done")


# class A :
#   data = []
# class B(A):
#   pass
# class C(A):
#   pass
# B.data.append(10)
# print(A.data,C.data)


# n = [1,2,3]
# r = map(lambda x: x+1 , n)
# print(r)

# class A :
#   data = []
# a = A()
# b = A()

# a.data.append(5)
# print(b.data)

# t = (1,2,3)
# t[0] = 5
# print(t) 


# class A :
#   x = 5
# a= A()
# b = A()
# a.x = 20
# print(A.x,a.x,b.x)


# class A :
#   def f(self):
#     return 1

# a = A()
# print(A.f(a), a.f())

# class A :
#   def f(self):
#     return "A"
# a = A()
# A.f = lambda self : "B"
# print(a.f())



# x = (5)
# y = (5,)
# print(type(x),type(y))


# x = 5 
# if x > 3 or x / 0 :
#   print("a")
# else :
#   print("b")


# clcoding = [1,2,3,4]
# result = filter(lambda x : x > 2 , clcoding)
# print(result)

# nums = [1,2,3]
# m = map(lambda x: x+10 , nums)
# print(next(m))
# print(next(m))
# nums.append(4)
# print(sum(m))

# c = [1,2,3]
# print(c.append(4))


# lst = [ 1,2,3,4]
# for i in range(len(lst)):
#   lst[i] += i
# print(lst)


