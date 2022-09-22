def max_end3(nums):
    number = 0
    #given that the length is 3, we can use indices 0 and 2 to compare
    # the first and last elements, and compare them
    if nums[0] >= nums[2]:
        number = nums[0]
    else:
        number = nums[2]
    #set the variable number to which one is greater, and create array to
    # repeat number three times
    return [number, number, number]

print(max_end3([1, 2, 3])) # [3, 3, 3]
print(max_end3([11, 5, 9])) # [11, 11, 11]
print(max_end3([2, 11, 3])) # [3, 3, 3]