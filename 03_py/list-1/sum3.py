def sum3(nums):
    #given that the length is 3 ints, we can simply add each val by
    # finding the values at each index (0, 1, 2)
    return nums[0] + nums[1] + nums[2]
    
print(sum3([1, 2, 3])) # 6
print(sum3([5, 11, 2])) # 18
print(sum3([7, 0, 0])) #7