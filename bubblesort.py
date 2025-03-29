def bubble(arr):
  n = len(arr)
  for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
      if arr[j] > arr[j+1]:
        arr[j] ,arr[j+1]  = arr[j+1] , arr[j]
        swapped = True

arr = [12,34,2,1,3,5,8]

bubble(arr)
print("sorted arr:",arr)
