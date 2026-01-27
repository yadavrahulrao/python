# bubble sort
arr = [2,3,4,567,8,9,7]
x = len(arr)
for i in range(0,x-1):
  for j in range(0,x-1-i):
    if arr[j] > arr[j+1]:
      temp = arr[j]
      arr[j] = arr[j+1]
      arr[j+1] = temp
print(arr)