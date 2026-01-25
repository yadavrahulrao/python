arr = [1,2,3,5,576,23,6]
n = int(input("enter the number:"))
x = len(arr)
for i in range(0,x):
  if arr[i] == n : 
    print("element is found",i)
  # else :
  #   print("not found")
