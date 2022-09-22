def make_ends(nums):
    #unknown length, so we can use the len function. Subtract 1 from
    # the length, to get the index of the last val.
    # Create a new array with nums[0], which we know is the first element
    # of the original array and nums[len(nums)-1]
    return [nums[0], nums[len(nums)-1]]
    
print() # [1, 3]
print() # [1, 4]
print() # [7, 2]