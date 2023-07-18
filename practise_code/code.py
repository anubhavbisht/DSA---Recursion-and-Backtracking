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

# ---------------------------------------------------------------------------- #
#                                tower of hanoi                                #
# ---------------------------------------------------------------------------- #
def towerOfHanoi(numberOfDiscs,source,destination,helper):
  if(numberOfDiscs==0):
    return
  towerOfHanoi(numberOfDiscs-1,source,helper,destination)
  print('Move disc:{} from tower->{} to tower-{}'.format(numberOfDiscs,source,destination))
  towerOfHanoi(numberOfDiscs-1,helper,destination,source)
towerOfHanoi(3,'A','B','C')

# ---------------------------------------------------------------------------- #
#                           display contents of array                          #
# ---------------------------------------------------------------------------- #
def displayArray(array,index):
  if(index==len(array)):
    return
  print(array[index])
  displayArray(array,index+1)
array = [1,3,4,5,2]
displayArray(array,0)

# ---------------------------------------------------------------------------- #
#                     display contents of array in reverse                     #
# ---------------------------------------------------------------------------- #
def displayArrayInReverse(array,index):
  if(index==len(array)):
    return
  displayArrayInReverse(array,index+1)
  print(array[index])
array = [1,3,4,5,2]
displayArrayInReverse(array,0)

# ---------------------------------------------------------------------------- #
#                              maximum of an array                             #
# ---------------------------------------------------------------------------- #
def maxOfArray(array,index):
  if(index==len(array)):
    return float('-inf')
  result = maxOfArray(array, index+1)
  if(result>array[index]):
    return result
  return array[index]
array = [-1,-3,-4,-5,-2]
print(maxOfArray(array,0))

# ---------------------------------------------------------------------------- #
#                           first index of occurrence                          #
# ---------------------------------------------------------------------------- #
def firstOccurrence(array,index,data):
  if(index==len(array)):
    return -1
  result = firstOccurrence(array, index+1,data)
  if(array[index]==data):
    return index
  return result
array = [2,3,6,9,8,1,4,5,8,0,8]
print(firstOccurrence(array,0,8))

# ---------------------------------------------------------------------------- #
#                  optimised way -> first index of occurrence                  #
# ---------------------------------------------------------------------------- #
def firstOccurrence(array,index,data):
  if(index==len(array)):
    return -1
  if(array[index]==data):
    return index
  result = firstOccurrence(array, index+1,data)
  return result
array = [2,3,6,9,8,1,4,5,8,0,8]
print(firstOccurrence(array,0,8))

# ---------------------------------------------------------------------------- #
#                           last index of occurrence                           #
# ---------------------------------------------------------------------------- #
def lastOccurrence(array,index,data):
  if(index==len(array)):
    return -1
  result = lastOccurrence(array, index+1,data)
  if(array[index]==data and result==-1):
    return index
  return result
array = [2,3,6,9,8,1,4,5,8,3,8]
print(lastOccurrence(array,0,3))
