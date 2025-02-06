list1 = [1,2,3,4,5,6]
s = list(map(lambda x:pow(x,2),list1))
print(s)
r = list(filter(lambda x:x%2==0 ,list1))
print(r)