# ---------------------------------------------------------------------------- #
#                 Print decreasing number starting from given n                #
# ---------------------------------------------------------------------------- #
def decreasingNumber(x):
  if (x==0):
    return
  print(x)
  decreasingNumber(x-1)
decreasingNumber(5)