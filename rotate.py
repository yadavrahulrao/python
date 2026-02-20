# def rotate(nums,k):
#   n = len(nums)
#   k %= n
#   def rev(i,j):
#     while i<j:
#       nums[i],nums[j] = nums[j] , nums[i]
#       i+= 1
#       j -= 1
#   rev(0,n-1)
#   rev(0,k-1)
#   rev(k,n-1)

# nums = [1,2,3,4,5,6,7]
# rotate(nums,3)
# print(nums)



class Solution :
  def rotate(self , nums:list , k : int) -> list :
    n = len(nums)
    res = []

    i = k
    while k<= i and i <= n-1 :
      res.append(nums[i])
      i +=1
    
    j = 0
    while j < k:
      res.append(nums[j])
      j+=1
    
    return res

s = Solution()
nums = [1,2,3,4,5,6]
k = 2
print(s.rotate(nums,k))
