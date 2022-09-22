#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  newstr = ""
  for x in range(len(str)): 
    if x % 2 == 0 : #all indices that are included are even
      newstr += str[x:x+1]
      
  return newstr

'''
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''