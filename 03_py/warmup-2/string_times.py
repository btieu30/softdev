#Given a string and a non-negative int n, return a larger string that is n copies of the original string.

def string_times(str, n):
  newstr = ""
  for x in range(n) : #for loops, you need to do range(num) instead of for x in n
    newstr += str 
    
  return newstr
  
'''
string_times('Hi', 2) → 'HiHi' 
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
'''