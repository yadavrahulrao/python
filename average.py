# program to find an average of N numbers .

n=5
sum=0
count=0
while count<n:
    number=float(input(" "))
    sum=sum +number  
    count=count+1
average = float(sum)/n    
print("n = %d , sum = %f" %(n ,sum))
print("Average  = %f"  % (average))
