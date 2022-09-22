
#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
  count = 0
  if len(a) < len(b) : 
    for x in range(len(a)-1) : #the number of times the for loop is run is the length of the smaller string
      if a[x:x+2] == b[x:x+2] : #checks if two indices for both strings are equal
        count +=1
  else :
    for x in range(len(b) - 1) :
      if a[x:x+2] == b[x:x+2] :
        count +=1
  return count

  
'''
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0def string_match(a, b):
'''
