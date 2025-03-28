def binary(arr , target ):
  left , right = 0 , len(arr) -1
  while left <= right :
    mid = (left + right)// 2

    if arr[mid] == target :
      return mid 
    elif arr[mid] > target: 
      right =  mid -1
    else :
      left = mid +1
  return -1
arr = [2,3,4,5,6,12,34,56]
target = 12
result = binary(arr ,target)

print("element found at index :",result)