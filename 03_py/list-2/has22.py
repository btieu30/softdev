def has22(nums):
    for x in range(len(nums) - 1):
        #for each entry in nums, check each value and its right neighbor
        if (nums[x] == 2 and nums[x+1] == 2):
            #if both are 2, return true
            return True
    #else, return false
    return False
    
print (has22([1, 2, 2]))
print (has22([1, 2, 1, 2]))
print (has22([2, 1, 2]))