#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  thenum = 0
  thestr = str[len(str)-2:] #the string that we are comparing the rest of the string to 
  for x in range(len(str) - 2) : #the last two chars do not count
    if str[x: x+2] == thestr:  
      thenum += 1 #adds one to the answer if any two letters are the same as the last two letters
      
  return thenum

'''
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''