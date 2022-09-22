def first_last6 (nums):
    #check if the last or first val in nums is equal to 6
    #last val is index len(nums) - 1, as indexing begins from 0 within an array
    if nums[len(nums) - 1] == 6 or nums[0] == 6:
        #if either is true, return True; else, return False
        return True
    return False

print(first_last6([1, 2, 6])) # True
print(first_last6([6, 1, 2, 3])) # False
print(first_last6([13, 6, 1, 2, 3])) #False