def first(arr,target):
  left , right = 0 , len(arr) -1
  while left <= right :
    mid = (left+right)//2
    if arr[mid]< target :
      left = mid +1
    elif arr[mid]>target:
      right = mid -1
    else :
      if mid == 0 or arr[mid -1] != target:
        return mid 
      right = mid -1

  return -1

def last(arr, target):
  left , right = 0 , len(arr) -1
  while left <= right :
    mid = (left + right )//2
    if arr[mid] < target :
      left = mid +1
    elif arr[mid] > target :
      right = mid -1
    else : 
      if mid == len(arr)-1 or arr[mid + 1] != target :
        return mid 
      left = mid +1
  return -1

def count(arr,target):
  a = first(arr,target)
  if a == -1:
    return 0
  
  b = last(arr,target)
  return b - a + 1

arr = [1,2,2,2,3]
target = 2
c = count(arr,target)
print(f"the target {target} ocuurs {c} times.")
  