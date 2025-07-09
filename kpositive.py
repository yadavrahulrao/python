def positive(arr,k):
  missing = 0
  current = 1
  i = 0
  while missing < k:
    if i < len(arr) and arr[i] == current :
      i += 1
    else :
      missing += 1
      if missing == k:
        return current
    current +=1
  return -1
arr = [1,2,4,5,7,9]
k = 2
c = positive(arr,k)
print(f"{k} missing element in array is :{c}")
