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

# ---------------------------------------------------------------------------- #
#                             all indices in array                             #
# ---------------------------------------------------------------------------- #
def allOccurrences(array,data,currentIndex):
  if(currentIndex==len(array)):
    return []
  occurencesArray = allOccurrences(array,data,currentIndex+1)
  if(array[currentIndex]==data):
    occurencesArray.append(currentIndex)
  return occurencesArray
    
array = [2,3,6,9,3,8,1,4,5,8,3,8]
print(allOccurrences(array,3,0))

# ---------------------------------------------------------------------------- #
#                       get all subsequences of a string                       #
# ---------------------------------------------------------------------------- #
string = "abc"
subsequences = ['']
for i in range(len(string)):
  newSubsequences = subsequences
  for j in range(len(subsequences)):
    newString = subsequences[j]+string[i]
    newSubsequences.append(newString)
  subsequences = newSubsequences
print(subsequences)

def subsequences(string):
  if(len(string)==0):
    return ['']
  firstChar = string[0]
  restOfString = string[1:]
  restOfCases = subsequences(restOfString)
  allCases = []
  for i in restOfCases:
    allCases.append(i)
    allCases.append(firstChar+i)
  return allCases
allStrings = subsequences("abc")
print(allStrings)

# ---------------------------------------------------------------------------- #
#                  Print all possible words from phone digits                  #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#     https://leetcode.com/problems/letter-combinations-of-a-phone-number/     #
# ---------------------------------------------------------------------------- #
class Solution:
    def alphabetsPossible(self, number:int) -> str:
        hashTable = ["", "", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]
        return hashTable[number]
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits)==0):
            return []
        else:
            firstChar = digits[0]
            restOfString = digits[1:]
            casesPossibleExcludingFirstChar = self.letterCombinations(restOfString)
            allCasesIncludingFirstChar = []
            if(len(casesPossibleExcludingFirstChar)==0):
                casesPossibleExcludingFirstChar.append('')
            for i in casesPossibleExcludingFirstChar:
                stringAtThatNumber = self.alphabetsPossible(int(firstChar))
                for j in stringAtThatNumber:
                    newCase = j+i
                    allCasesIncludingFirstChar.append(newCase)
            return allCasesIncludingFirstChar

# ---------------------------------------------------------------------------- #
#                                Climbing Stairs                               #
# ---------------------------------------------------------------------------- #
def stairPath(numberOfStairs):
  if(numberOfStairs==0):
    return []
  else:
    numberOfPathsPossibleFromThatStair = []
    if(numberOfStairs-3 <= 0):
      maxDepth = 0
    else:
      maxDepth = numberOfStairs-3
    for i in range (numberOfStairs-1,maxDepth-1,-1):
      casesPossibleFromLowerStair = stairPath(i)
      if(len(casesPossibleFromLowerStair)==0):
        numberOfPathsPossibleFromThatStair.append(str(numberOfStairs))
      else:
        for j in casesPossibleFromLowerStair:
          numberOfPathsPossibleFromThatStair.append(str(numberOfStairs-i)+j)
    return numberOfPathsPossibleFromThatStair
print(stairPath(7))

def stairPath(numberOfStairs):
  if(numberOfStairs==0):
    return ['']
  if(numberOfStairs<0):
    return []
  else:
    numberOfPathsPossibleFromThatStair = []
    path1 = stairPath(numberOfStairs-1)
    path2 = stairPath(numberOfStairs-2)
    path3 = stairPath(numberOfStairs-3)
    for i in path1:
      numberOfPathsPossibleFromThatStair.append('1'+i)
    for i in path2:
      numberOfPathsPossibleFromThatStair.append('2'+i)
    for i in path3:
      numberOfPathsPossibleFromThatStair.append('3'+i)
    return numberOfPathsPossibleFromThatStair
print(stairPath(0))

# ---------------------------------------------------------------------------- #
#                                get maze paths                                #
# ---------------------------------------------------------------------------- #
def getMazePaths(sourceCol,sourceRow,destinationCol,destinationRow):
  if(sourceCol==destinationCol and sourceRow==destinationRow):
    return []
  else:
    pathPossibleFromCurrentLocation = []
    if(sourceCol+1<=destinationCol):
      moveOneColumn = getMazePaths(sourceCol+1,sourceRow,destinationCol,destinationRow)
      if(len(moveOneColumn)==0):
        pathPossibleFromCurrentLocation.append('h')
      else:
        for i in moveOneColumn:
          pathPossibleFromCurrentLocation.append('h'+i)
    if(sourceRow+1<=destinationRow):
      moveOneRow = getMazePaths(sourceCol,sourceRow+1,destinationCol,destinationRow)
      if(len(moveOneRow)==0):
        pathPossibleFromCurrentLocation.append('v')
      else:
        for i in moveOneRow:
          pathPossibleFromCurrentLocation.append('v'+i)
    return pathPossibleFromCurrentLocation
paths = getMazePaths(1,1,3,3)
print(paths)

# ---------------------------------------------------------------------------- #
#           Maze paths with jumps(vertically,diagnally,,horizontally)          #
# ---------------------------------------------------------------------------- #
def getMazePaths(sourceCol,sourceRow,destinationCol,destinationRow):
  if(sourceCol==destinationCol and sourceRow==destinationRow):
    return []
  else:
    pathPossibleFromCurrentLocation = []
    ##horizonatlly
    for i in range(1,destinationCol):
      if(sourceCol+i<=destinationCol):
        moveColumnByIth = getMazePaths(sourceCol+i,sourceRow,destinationCol,destinationRow)
        if(len(moveColumnByIth)==0):
          pathPossibleFromCurrentLocation.append('h'+str(i))
        else:
          for j in moveColumnByIth:
            pathPossibleFromCurrentLocation.append('h'+str(i)+j)
      else:
        break        
    ##vertically
    for i in range(1,destinationRow):
      if(sourceRow+i<=destinationRow):
        moveRowByIth = getMazePaths(sourceCol,sourceRow+i,destinationCol,destinationRow)
        if(len(moveRowByIth)==0):
          pathPossibleFromCurrentLocation.append('v'+str(i))
        else:
          for j in moveRowByIth:
            pathPossibleFromCurrentLocation.append('v'+str(i)+j)
      else:
        break
    ##diagonally
    for i in range(1,min(destinationCol,destinationRow)):
      if(sourceRow+i<=destinationRow and sourceCol+i<=destinationCol):
        moveDiagonallyByIth = getMazePaths(sourceCol+i,sourceRow+i,destinationCol,destinationRow)
        if(len(moveDiagonallyByIth)==0):
          pathPossibleFromCurrentLocation.append('d'+str(i))
        else:
          for j in moveDiagonallyByIth:
            pathPossibleFromCurrentLocation.append('d'+str(i)+j)
      else:
        break
    return pathPossibleFromCurrentLocation
paths = getMazePaths(1,1,3,3)
print(paths)

# ---------------------------------------------------------------------------- #
#                              print subsequences                              #
# ---------------------------------------------------------------------------- #
def printSubsequences(string,substring):
  if(len(string)==0):
    print(substring)
    return
  else:
    firstCharacter = string[0]
    restOfString = string[1:]
    printSubsequences(restOfString,substring+firstCharacter)
    printSubsequences(restOfString,substring)
parentString = 'abc'
printSubsequences(parentString,'')
