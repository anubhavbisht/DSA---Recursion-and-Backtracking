# ---------------------------------------------------------------------------- #
#                 Print decreasing number starting from given n                #
# ---------------------------------------------------------------------------- #
def decreasingNumber(x):
  if (x==0):
    return
  print(x)
  decreasingNumber(x-1)
decreasingNumber(5)

# ---------------------------------------------------------------------------- #
#                 Print increasing number starting from given n                #
# ---------------------------------------------------------------------------- #

def increasingNumber(x):
  if (x==0):
    return
  increasingNumber(x-1)
  print(x)
increasingNumber(10)