#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

def array_front9(nums):
  if len(nums) < 4 : #base case: if the array length is less than 4, all indices are traversed
    for x in range(len(nums)) :
      if nums[x] == 9 : 
        return True
  else :
     for x in range(4) : #checks the first 4 indices for arrays longer than length 4
      if nums[x] == 9 :
        return True
  
  return False
    
'''
array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''