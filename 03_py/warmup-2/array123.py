#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

def array123(nums):
  num = 0
  for x in range(len(nums) - 2) :
    if nums[x] == 1 and nums[x+1] == 2 and nums[x+2] ==3 : #checks if any three consecutive indices are 1, 2 and 3
      return True
      
  return False

'''
array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''