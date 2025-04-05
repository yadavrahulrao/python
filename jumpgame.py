def canJump(nums):
    farthest = 0  
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            return True
    return False
nums = [2, 3, 1, 1, 4]
print(canJump(nums))  

nums = [3, 2, 1, 0, 4]
print(canJump(nums))  
