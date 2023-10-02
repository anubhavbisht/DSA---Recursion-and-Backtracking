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

# ---------------------------------------------------------------------------- #
#                           print keypad combinations                          #
# ---------------------------------------------------------------------------- #
def alphabetsPossible(number):
  hashTable = ["", "", "abc", "def", "ghi", "jkl",
       "mno", "pqrs", "tuv", "wxyz"]
  return hashTable[number]
def keypadCombinations(question,answer):
  if(len(question)==0):
      print(answer)
      return
  else:
      firstDigit = question[0]
      restOfMobileNumber = question[1:]
      charactersPossibleByFirstDigit = alphabetsPossible(int(firstDigit))
      for j in charactersPossibleByFirstDigit:
        answer+=j
        keypadCombinations(restOfMobileNumber,answer)  
parentString = '23'
keypadCombinations(parentString,'')

# ---------------------------------------------------------------------------- #
#                               print stair path                               #
# ---------------------------------------------------------------------------- #
def stairPaths(numberOfStairs,path):
  if(numberOfStairs==0):
      print(path)
      return
  else:
      if(numberOfStairs-1)>=0:
        stairPaths(numberOfStairs-1,path+'1')
      if(numberOfStairs-2)>=0:
        stairPaths(numberOfStairs-2,path+'2')
      if(numberOfStairs-3)>=0:
        stairPaths(numberOfStairs-3,path+'3')
parentStep = 4
stairPaths(parentStep,'')
      
# ---------------------------------------------------------------------------- #
#                               print maze paths                               #
# ---------------------------------------------------------------------------- #
def mazePaths(sourceCol,sourceRow,destinationCol,destinationRow,path):
  if(sourceCol==destinationCol and sourceRow==destinationRow):
      print(path)
      return
  else:
      if(sourceCol+1<=destinationCol):
        mazePaths(sourceCol+1,sourceRow,destinationCol,destinationRow,path+'h')
      if(sourceRow+1<=destinationRow):
        mazePaths(sourceCol,sourceRow+1,destinationCol,destinationRow,path+'v')
mazePaths(1,1,4,4,'')

# ---------------------------------------------------------------------------- #
#        print maze paths with jumps(horizontally,diagonally,vertically)       #
# ---------------------------------------------------------------------------- #
def printMazePathsWithJumps(sourceCol,sourceRow,destinationCol,destinationRow,path):
  if(sourceCol==destinationCol and sourceRow==destinationRow):
    print('Path ->',path)
    return
  ##vertically
  for i in range(1,destinationRow):
    if(sourceRow+i<=destinationRow):
      printMazePathsWithJumps(sourceCol,sourceRow+i,destinationCol,destinationRow,path+'v'+str(i))
    else:
      break
  ##horizontally
  for j in range(1,destinationCol):
    if(sourceCol+j<=destinationCol):
      printMazePathsWithJumps(sourceCol+j,sourceRow,destinationCol,destinationRow,path+'h'+str(j))
    else:
      break
  ##diagonally
  for k in range(1,min(destinationCol,destinationRow)):
    if(sourceCol+k<=destinationCol and sourceRow+k<=destinationRow):
      printMazePathsWithJumps(sourceCol+k,sourceRow+k,destinationCol,destinationRow,path+'d'+str(k))
    else:
      break
printMazePathsWithJumps(1,1,4,4,'')

# ---------------------------------------------------------------------------- #
#                         print permutations of string                         #
# ---------------------------------------------------------------------------- #
def printPermutations(question,possibleAnswer):
  if(len(question)==0):
    print(possibleAnswer)
    return
  else:
    for i in range(len(question)):
      character = question[i]
      leftString = question[0:i]
      rightString = question[i+1:]
      combinedString = leftString+rightString
      printPermutations(combinedString, possibleAnswer+character)
printPermutations('abc','')

# ---------------------------------------------------------------------------- #
#                                print encodings                               #
# ---------------------------------------------------------------------------- #
def printEncodings(question,possibleAnswer):
  if(len(question)==0):
    print(possibleAnswer)
    return
  else:
    for i in range(len(question)):
      leftString = question[0:i+1]
      if(leftString[0]=='0'):
        return 
      if(int(leftString)<=26):
        rightString = question[i+1:]
        printEncodings(rightString,possibleAnswer+chr(int(leftString)+96))
      else:
        break
printEncodings('303','')

# ---------------------------------------------------------------------------- #
#                                   floodfill                                  #
# ---------------------------------------------------------------------------- #
class Solution:
    def ff(self,image,sr,sc,newColor,prevColor,row,col):
        ##base case
        if (sr<0 or sc<0 or sr>=row or sc>=col or image[sr][sc]!=prevColor or image[sr][sc]==newColor):
            return
        image[sr][sc]=newColor
        self.ff(image,sr+1,sc,newColor,prevColor,row,col)
        self.ff(image,sr-1,sc,newColor,prevColor,row,col)
        self.ff(image,sr,sc+1,newColor,prevColor,row,col)
        self.ff(image,sr,sc-1,newColor,prevColor,row,col)
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row=len(image)
        col=len(image[0])
        prevColor=image[sr][sc]
        self.ff(image,sr,sc,newColor,prevColor,row,col)
        return image

# ---------------------------------------------------------------------------- #
#                               target sum subset                              #
# ---------------------------------------------------------------------------- #
def targetSumSubset(originalArray,targetSum,currentSubset,currentSum):
  if(currentSum==targetSum):
    print(currentSubset)
    return
  if(len(originalArray)==0 or currentSum>targetSum):
    return
  else:
    firstElementOfArray = originalArray[0]
    restOfArray = originalArray[1:]
    # not firstelem contri
    targetSumSubset(restOfArray,targetSum,currentSubset,currentSum)
    # if firstelem contri
    newSum = currentSum+firstElementOfArray
    currentSubset.append(firstElementOfArray)
    targetSumSubset(restOfArray,targetSum,currentSubset,newSum)
    currentSubset.pop()

array = [10,20,30,40,50]
target = 60
targetSumSubset(array,target,[],0)

# ---------------------------------------------------------------------------- #
#                                   n queens                                   #
# ---------------------------------------------------------------------------- #
def printBoard(nestedArray):
  for i in nestedArray:
    print(i)

def checkValidPosition(checkList, column, row, totalLength):
  startingRow = row
  startingColumn = column
  ##checking vertically
  while (startingRow >= 0):
    if (checkList[startingRow][column] == True):
      return False
    startingRow -= 1
  startingRow = row
  ##checking right diagonally
  while (startingRow >= 0 and startingColumn >= 0
         and startingColumn < totalLength):
    if (checkList[startingRow][startingColumn] == True):
      return False
    startingRow -= 1
    startingColumn += 1
  startingRow = row
  startingColumn = column
  ##checking left diagonally
  while (startingRow >= 0 and startingColumn >= 0):
    if (checkList[startingRow][startingColumn] == True):
      return False
    startingRow -= 1
    startingColumn -= 1
  return True

def queenSetup(chessBoard, checkList, currentRow, totalRows):
  if (currentRow >= totalRows):
    printBoard(chessBoard)
    print('******************************')
    print('******************************')
  else:
    #traversing column
    for col in range(0, totalRows):
      if (checkValidPosition(checkList, col, currentRow, totalRows)):
        chessboard[currentRow][col] = 'Q'
        checkList[currentRow][col] = True
        queenSetup(chessBoard, checkList, currentRow + 1, totalRows)
        chessboard[currentRow][col] = '|X|'
        checkList[currentRow][col] = False

print('This is n queen problem')
n = int(input("Please enter value of n:"))
chessboard = [['|X|' for i in range(n)] for j in range(n)]
checkList = [[False for i in range(n)] for j in range(n)]
print('We have {0}X{1} chessboard'.format(n, n))
printBoard(chessboard)
print('Now we have to place {0} queens into this board'.format(n))
print('Given below are desired results')
queenSetup(chessboard, checkList, 0, n)

# ---------------------------------------------------------------------------- #
#                                 knights tour                                 #
# ---------------------------------------------------------------------------- #
def knightTour(checkList, currentRow, currentColumn, totalSize,
               movesTakenTillNow, squaresCovered):
  if (squaresCovered == totalSize * totalSize):
    print('Moves list', movesTakenTillNow)
    print('******************************')
    print('******************************')
    return
  else:
    ## if your knight is at ith row and jth column you can take atmost 8 moves from that position
    positions = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2],
                 [-2, -1]]
    for i in positions:
      posX = i[0]
      posY = i[1]
      if (currentRow + posX >= 0 and currentRow + posX < totalSize
          and currentColumn + posY < totalSize and currentColumn + posY >= 0
          and checkList[currentRow + posX][currentColumn + posY] == False):
        checkList[currentRow + posX][currentColumn + posY] = True
        squaresCovered += 1
        move = '(X{},Y{}->>X{},Y{})'.format(currentRow, currentColumn,
                                            currentRow + posX,
                                            currentColumn + posY)
        movesTakenTillNow.append(move)
        knightTour(checkList, currentRow + posX, currentColumn + posY,
                   totalSize, movesTakenTillNow, squaresCovered)
        checkList[currentRow + posX][currentColumn + posY] = False
        squaresCovered -= 1
        movesTakenTillNow.pop()

print('This is a knight tour problem')
n = int(input("Please enter value of n:"))
checkList = [[False for i in range(n)] for j in range(n)]
print('We have {0}X{1} chessboard and knight has to cover {2} squares'.format(
  n, n, n * n))
print('Enter your knight starting position')
startingX = int(input('Enter X coordinate:'))
startingY = int(input('Enter Y coordinate:'))
print('Given below are desired moves to fulfill this')
checkList[startingX][startingY] = True
knightTour(checkList, startingX, startingY, n, [], 0)
