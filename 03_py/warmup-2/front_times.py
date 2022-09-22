#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(str, n):
  newstr = ""
  if len(str) <3 :
    for x in range(n) :
      newstr += str #the string is concatenated to itself n times 
  else :
    for x in range(n):
      newstr += str[0:3] #the string's first 3 chars is concatenated n times
  return newstr

'''
front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
'''