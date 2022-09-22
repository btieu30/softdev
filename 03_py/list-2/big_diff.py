def big_diff(nums):
    #max and min begin at the same point
    maximum = nums[0]
    minimum = nums[0]
    
    #iterate through nums to find the max and min by continously comparing 
    #values and setting them equal to the maximum and minimum variables
    for x in nums:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    #subtract the min from the max
    return maximum - minimum

print(big_diff([10, 3, 5, 6])) # 7
print(big_diff([7, 2, 10, 9])) # 8
print(big_diff([2, 10, 7, 2])) # 8