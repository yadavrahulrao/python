# arr = [1,2,3,45,78,888]
# x = len(arr)
# n = int(input("enter the number :"))
# def binary(arr,n):
#   low = 0
#   high = x -1 
#   while low <= high :
#     mid = (low+ high)//2
#     if arr[mid] == n :
#       return mid
#     elif arr[mid] < n :
#       low = mid + 1
#     else :
#       high = mid - 1 
#   return -1
# print(binary(arr,n))


# for binary search array should be sorted 


arr = [1,2,3,4,56]
x = len(arr)
n = int(input("enter the number :"))

low = 0
high = x -1
for i in range (x):
  mid = (low+high)//2
  if arr[mid] == n :
    print("no found",mid)
    break
  elif arr[mid] < n :
    low = mid + 1
  else :
    high = mid - 1
else :
  print("element not found")
