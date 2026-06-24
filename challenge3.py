# x = b"ABC"
# print(x[0])


# class test:
#   x = 10 

# obj = test()
# obj.x = 50 
# print(test.x)
# print(obj.x)


# print(sum(range(5)))


# num = [1,2,3,4,5]

# cube = [x**3 for x in num]

# print(cube)

# sums = lambda x : (x*(x+1))/2
# x = 10
# print(sums(x))


# print(0.1 + 0.3 == 0.4)



# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# permu = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

# print(permu)


# for i in range(4):
#     for j in range(4):
#         print('*',end='')
#     print()
        

# for i in range(5):
#     for j in range(i):
#         print('*',end='')
#     print()

# for i in range(1,5):
#     for j in range(1,i):
#         print(j,end='')
#     print()
    
# for i in range(5):
#     for j in range(i):
#         print(i,end='')
#     print()
    
    
# for i in range(5):
#     for j in range(5-i+1):
#         print('*',end='')
#     print()
    

# for i in range(5):
#     for j in range(5-i+1):
#         print(j,end='')
#     print()


# for i in range(6):
#     for j in range(6-i-1):
#         print(' ',end='')
    
#     for j in range(2*i+1):
#         print('*',end='')
        
#     for j in range(6-i-1):
#         print(' ',end='')
    
#     print()
        
# for i in range(7):
#     for j in range(i):
#         print(' ',end='')
#     for j in range((2*7)- (2*i + 1)):
#         print('*',end='')
#     for j in range(i):
#         print(' ',end='')
        
#     print()


n = int(input())

# for i in range(2*n -1 ):
#     s = i
#     if i > n :
#         s = 2 *n -i 
#     for j in range(s):
#         print('*',end='')
#     print()


# s = 1 
# for i in range(n):
#     if i % 2 == 0 :
#         s = 1
#     else :
#         s = 0
#     for j in range(i):
#         print(s,end='')
#         s = 1-s
#     print()
        
# s = 2 *(n-1)
# for i in range(n):
#     # number
#     for j in range(i):
#         print(j,end='')
    
#     # space
#     for j in range(s):
#         print(" ",end='')
    
    
#     # number
#     for j in reversed(range(i)):
#         print(j,end='')
#     s -= 2
#     print()



# s = 0
# for i in range(n):
#     for j in range(i):
#         print(s,end='')
#         s = s+1
#     print()


# for i in range(n):
#     ac = ord('A')
#     for j in range(ac , ac + i):
#         print(chr(j),end='')
#     print()


# for i in range(n):
#     ac = ord('A')
#     for j in range(ac , ac + n- i - 1):
#         print(chr(j),end='')
#     print()

# for i in range(0,n):
#     ac = ord('A') + i
#     for j in range(0,i):
#         print(chr(ac),end='')
#     print()


# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end='')
#     ac = ord('A')
#     s = (2*i+1) / 2    
#     for j in range(2*i+1):
#         print(chr(ac),end='')
#         if j <= s :
#             ac += 1
#         else :
#             ac -= 1
        
    
#     for j in range(n-i-1):
#         print(' ',end='')
        
#     print()


# for i in range(n):
#     ac = ord('E')
#     for j in range(ac-i , ac):
#         print(chr(ac),end='')
#     print()
    
    
# s = 0 
# for i in range(n):
#     for j in range(n-i):
#         print('*',end='')
#     for j in range(s):
#         print(' ',end='')
#     for j in range(n-i):
#         print('*',end='')
#     s += 2
#     print()
    
# s = 8
# for i in range(n):
#     for j in range(i):
#         print('*',end='')
#     for j in range(s):
#         print(' ',end='')
#     for j in range(i):
#         print('*',end='')
#     s -= 2
#     print()
    
# p = 2 * n - 2  
# for i in range(2*n -1 ):
#     s = i 
#     if i > n :
#         s = 2 *n -i
#     for j in range(s):
#         print('*',end='')
#     for j in range(p):
#         print(' ',end='') 
#     for j in range(s):
#         print('*',end='')
#     print()
#     if i < n :
#         p -= 2
#     else :
#         p += 2
    
    


# for i in range(n):
#     for j in range(n):
#         if (i == 0) or (j == 0) or (i ==  n-1)  or (j == n -1) :
#             print('*',end='')
            
#         else:
#             print(' ',end='') 
#     print()
        
        
    
for i in range(2 * n - 1):
    for j in range(2 *n - 1):
        top = i
        left = j 
        right = (2*n - 2)-j
        bot = (2*n - 2) - i
        print(n-min(min(top,bot),min(left,right)),end='')
    print()
        
    
