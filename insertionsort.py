def insertion(arr):
  for i in range(1 , len(arr)):
    key = arr[i]
    j = i-1
    while j>= 0 and arr[j]> key :
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
arr = [12 ,56 ,78, 98,1 ,2,8]
insertion(arr)
print("sorted array:",arr)