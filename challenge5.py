# recursion 
# c = 0
# def f(c):
#     if c == 3:
#         return 
#     print(c)
#     c+= 1
#     f(c)
# f(1)


# c = 0 
# def f(c):
#     print(c)
#     c += 1
#     f(c)
    
# f(c)

# n = int(input("enter name :"))
# c = 0
# def name(c,n):
#     if c == n :
#         return 
#     print("rahul")
#     c += 1
#     name(c,n)
    
# name(c,n)
    


# n = int(input("enter n :"))
# c= 0
# def f(c):
#     if c == n:
#         return
#     print(c)
     
#     c += 1
#     f(c)
    
# f(c)


def f(i,n):
    if i < n :
        return 
    f(i-1,n)
    print(i)
    
f(4,3)