def centered_average(nums):
    #min and max begin at the same point
    maximum = nums[0]
    minimum = nums[0]
    
    #iterate through nums to find the min and max,
    #comparing and replacing x as we go
    for x in nums:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    
    #remove or "ignore" the smallest and largest nums in the array
    nums.remove(maximum)
    nums.remove(minimum)
    
    sum = 0
    #add up all the nums in the array
    for x in nums:
        sum += x
    
    #divide by the length to find the "centered average"
    return sum / len(nums)

print(centered_average([1, 2, 3, 4, 100])) # 3
print(centered_average([1, 1, 5, 5, 10, 8, 7])) # 5
print(centered_average([-10, -4, -2, -4, -2, 0])) # -3