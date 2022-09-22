def same_first_last(nums):
    #check if first and last val within nums are the same
    if nums[0] == nums[len(nums) - 1]:
        #if they are equal, return True; else, return False
        return True
    return False
    
print(same_first_last([1, 2, 3])) # False
print(same_first_last([1, 2, 3, 1])) # True
print(same_first_last([1, 2, 1])) # True