def sum2(nums):
    #if the array is empty, return 0
    if len(nums) == 0:
        return 0
    
    #if the array length is greater than length 2, only add the first 2
    elif len(nums) >= 2:
        return nums[0] + nums[1]
    
    #if the array length is less than 2, add up the elements that exist (the only element in the array)
    elif len(nums) == 1:
        return nums[0]

print(sum2([1, 2, 3])) # 3
print(sum2([1, 1])) # 2
print(sum2([1, 1, 1, 1])) # 2