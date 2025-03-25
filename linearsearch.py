def linear(arr , target):
  for i in range(len(arr)):
    if arr[i] == target :
      return i 
  return -1
arr = [12 , 3 , 4, 5 , 6 , 2]
target = 4
result = linear(arr , target)
print("element found at index :",result)
  