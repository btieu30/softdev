def rotate_left3(nums):
    #pop off the val at index 0, add it to the end of list
    nums.append(nums.pop(0))
    return nums
    
print(rotate_left3([1, 2, 3])) # [2, 3, 1]
print(rotate_left3([5, 11, 9])) # [11, 9, 5]
print(rotate_left3([7, 0, 0])) # [0, 0, 7]