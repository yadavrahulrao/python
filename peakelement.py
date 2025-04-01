def peak(arr):
  left , right = 0, len(arr) -1
  while left <= right :
    mid = (left + right)//2
    if (mid == 0 or arr[mid] > arr[mid - 1]) and ( mid == len(arr)-1 or arr[mid]> arr[mid +1]):
      return mid
    elif mid < len(arr)-1 and arr[mid]<arr[mid +1]:
      left = mid +1

    else :
      right = mid -1 
      
  return -1
arr = [1,2,6,20,4,3]
c = peak(arr)
print(f"peak element is :{arr[c]} at index {c}")