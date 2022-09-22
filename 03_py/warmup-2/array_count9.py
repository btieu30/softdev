#Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  thenum = 0
  for x in nums: 
    if x == 9 : #if any int inside the array is equal to 9, thenum is incremented
      thenum += 1
      
  return thenum

'''
array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''