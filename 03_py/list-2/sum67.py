def sum67(nums):
    total = 0
    canAdd = True #boolean to determine whether or not a value should be added to grand total
    for x in range(len(nums)):
        #if the num at index x is 6, it cannot be added to total
        if nums[x] == 6:
           canAdd = False
        #if the canAdd is False, but we reach 7, we expect the next val to be added to total, so we set canAdd to True
        elif canAdd == False and nums[x] == 7:
            canAdd = True
        #if the value can be added, add it to the total
        elif canAdd:
            total = total + nums[x]
    return total

print(sum67([1, 2, 2])) # 5
print(sum67([1, 2, 2, 6, 99, 99, 7])) # 5
print(sum67([1, 1, 6, 7, 2])) # 4