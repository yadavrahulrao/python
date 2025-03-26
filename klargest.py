def largest(arr,k):
  arr.sort(reverse = True)
  return arr[k-1]
arr = [1,4,6,23,56,2,78]
k = 3
c = largest(arr,k)
print(f"{k} largest element is :{c}")
