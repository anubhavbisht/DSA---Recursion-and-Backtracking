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

# ---------------------------------------------------------------------------- #
#              Print decreasing and increasing number from given n             #
# ---------------------------------------------------------------------------- #
def decreasingIncreasingNumber(x):
  if (x==0):
    return
  print(x)
  decreasingIncreasingNumber(x-1)
  print(x)
decreasingIncreasingNumber(5)

# ---------------------------------------------------------------------------- #
#                             Factorial of a number                            #
# ---------------------------------------------------------------------------- #
def factorial(x):
  if (x==0):
    return 1
  return x * factorial(x-1)
print(factorial(5))

# ---------------------------------------------------------------------------- #
#                               Power of a number                              #
# ---------------------------------------------------------------------------- #
def power(x,n):
  if (n==0):
    return 1
  return x * power(x,n-1)
print(power(2,5))

# ---------------------------------------------------------------------------- #
#               Power of a number in logarithmic time complexity               #
# ---------------------------------------------------------------------------- #
def powerInLogarithmicTime(x,n):
  if (n==0):
    return 1
  result = powerInLogarithmicTime(x,n//2)
  if (n%2==0):
    return result*result
  else:
    return x*result*result
print(powerInLogarithmicTime(2,5))