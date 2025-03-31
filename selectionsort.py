def selection(arr):
  for i in range (len(arr)):
    min = i
    for j in range (i+1,len(arr)):
      if arr[j] < arr[min]:
        min = j
    
    arr[i] , arr[min] = arr[min] , arr[i]

arr = [12,5,3,34,55,2]

selection(arr)
print("sorted array:",arr)