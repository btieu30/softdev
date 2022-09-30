def has23(nums):
    #given the length, check both indices (0 and 1) to check if either
    # equals to 2 or 3
    if nums[0] == 2 or nums[0] == 3 or nums[1] == 2 or nums[1] == 3:
        return True
    return False

print(has23([2, 5])) # True
print(has23([4, 3])) # True
print(has23([4, 5])) # False