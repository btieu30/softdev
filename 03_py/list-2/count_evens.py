def count_evens(nums):
    count = 0
    #iterate through nums, taking each val, if the val's division by 2
    # yields no remainder, increase the count
    for x in nums:
        if x % 2 == 0:
            count += 1
    
    #return the total count of even nums
    return count
    
print(count_evens([2, 1, 2, 3, 4])) # 3
print(count_evens([2, 2, 0])) # 3
print(count_evens([1, 3, 5])) # 0