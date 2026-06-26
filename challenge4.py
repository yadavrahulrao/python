# n = 1123
# time complexity - log10(n)
# count = 0
# while n > 0 :
#     digit = n % 10
#     count = count + 1
#     n = n // 10
    

# print(count)


# n = 727
# p = n

# r = 0 
# while n > 0 :
#     dig = n % 10
#     r = (r * 10) + dig
#     n = n // 10
  
# print(r==p)
# if int(p) != int(r) :
#     print("False")
    
# else :
#     print("True")n = 727


# n = 371
# s = str(n)
# l = [int(i) for i in s]
# len_n = len(l)
# lam = [x**len_n for x in l]
# o = sum(lam)
# print(o)


# n = 36

# for i in range(1,n+1):
#     if n % i == 0 :
#         print(i)



#LCM Program 

# num1 = int(input("enter 1st num:"))
# num2 = int(input("enter 2nd num:"))
# n = num1 * num2
# res1= [x * num1 for x in range(1,n)]
# for y in range(1,n):
#     if y * num2 in res1 :
#         print(y*num2)
#         break
# s = set()
# dup = set()
# for i in res1:
#     if i in s :
#         print(i)
#         break
#     else:
#         s.add(i)
# # print(min(dup))




# n = 5
# c = 0
# for i in range(1,n+1):
#     if n % i == 0 :
#         c += 1
    
# if c == 2 :
#     print("prime")
# else:
#     print("not prime ")
        
        
# num1 = int(input("enter the 1st num:"))
# num2 = int(input("enter the 2nd number:"))

# n = min(num1,num2)
# hcf = 1

# for i in range(1,n+1):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i
        
# print(hcf)
        
        
n1 = int(input("enter num1:"))
n2 = int(input("enter num2:"))

num1 = max(n1,n2)
num2 = min(n1,n2)
sub = num1 - num2

n = min(sub,num2)
hcf = 1
for i in range(1,n+1):
    if sub % i == 0 and num2 % i == 0 :
        hcf = i
print(hcf)