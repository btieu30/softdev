#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  newstr = ""
  for x in range(len(str)) :
    newstr += str[0:x+1] #Adds from the 0th index to the number of times it is currently being traversed index. 
    
  return newstr

'''
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''