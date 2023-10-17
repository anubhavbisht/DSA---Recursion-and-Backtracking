# ---------------------------------------------------------------------------- #
#                         1. Longest absolute file path                        #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
#    (https://leetcode.com/problems/longest-absolute-file-path/description/)   #
# ---------------------------------------------------------------------------- #
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        inputArray = input.split('\n')
        fileStack = []
        maxLength = 0
        for i in inputArray:
            depthOfCurrentElement = i.count('\t')
            lengthOfCurrentElement = 0
            if (len(fileStack) == 0 or depthOfCurrentElement == 0):
                lengthOfCurrentElement = len(i) - depthOfCurrentElement 
            else:
                if(depthOfCurrentElement<=fileStack[-1][0]):
                    while(len(fileStack) > 0 and fileStack[-1][0]>=depthOfCurrentElement):
                        fileStack.pop()
                lengthOfCurrentElement = len(i) - depthOfCurrentElement + fileStack[-1][1] +1
            if('.' in i):
                maxLength = max(lengthOfCurrentElement,maxLength)
            else:
                fileStack.append([depthOfCurrentElement,lengthOfCurrentElement]) #[number of \t i.e depth, length of string excluding \t]
        return maxLength

