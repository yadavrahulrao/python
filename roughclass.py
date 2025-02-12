a = input("enter string:")
b = input("enter string:")
count = 0 
for i in range(0,len(a)) :
            if b == a[i] :
                    print("found")
                    count = count+1
print(count)
