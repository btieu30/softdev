def pos_neg(a, b, negative):
  if negative == False :
    return a * b < 0
  else:
    return a < 0 and b < 0