# ------------------- 1. next greatest element to the right ------------------ #
array = [1,3,2,4]
answer = []
stack = []
for i in range(len(array)-1,-1,-1):
  while (len(stack)>0 and array[i]>stack[-1]):
    stack.pop()
  if (len(stack)==0):
    answer.append(-1)
  else:
    answer.append(stack[-1])
  stack.append(array[i])
print(answer[::-1])
# ------------------ 2. nearest greatest element to the left ----------------- #
array = [1,3,2,4]
answer = []
stack = []
for i in range(0,len(array)):
  while (len(stack)>0 and array[i]>stack[-1]):
    stack.pop()
  if (len(stack)==0):
    answer.append(-1)
  else:
    answer.append(stack[-1])
  stack.append(array[i])
print(answer)
# ---------------------- 3. nearest smaller element to the right --------------------- #
array = [1,3,2,5,4]
answer = []
stack = []
for i in range(len(array)-1,-1,-1):
  while (len(stack)>0 and array[i]<stack[-1]):
    stack.pop()
  if (len(stack)==0):
    answer.append(-1)
  else:
    answer.append(stack[-1])
  stack.append(array[i])
print(answer[::-1])
# ---------------------- 4. nearest smaller element to the left ---------------------- #
array = [1,3,2,5,4]
answer = []
stack = []
for i in range(0,len(array)):
  while (len(stack)>0 and array[i]<stack[-1]):
    stack.pop()
  if (len(stack)==0):
    answer.append(-1)
  else:
    answer.append(stack[-1])
  stack.append(array[i])
print(answer)
# --------------------------- 5. stock span problem -------------------------- #
array = [100,80,60,70,60,75,85]
answer = []
stack = []
for i in range(0,len(array)):
  consecutiveCount=1
  while (len(stack)>0 and array[i]>stack[-1][0]):
    consecutiveCount+=stack[-1][1]
    stack.pop()
  if (len(stack)==0):
    answer.append(1)
  else:
    answer.append(consecutiveCount)
  stack.append([array[i],consecutiveCount])
print(answer)
# ------------------------- 5. max area of histogram ------------------------- #
buildingHeights = [6,2,5,4,5,1,6]
nsr = []
nsl = []
stack = []
for i in range(len(buildingHeights)-1,-1,-1):
  while(len(stack)>0 and buildingHeights[i]<stack[-1][0]):
    stack.pop()
  index = None
  if(len(stack)==0):
    index = len(buildingHeights)
  else:
    index = stack[-1][1]
  nsr.append(index)
  stack.append([buildingHeights[i],i])
nsr = nsr[::-1]
stack = []
for i in range(0,len(buildingHeights)):
  while(len(stack)>0 and buildingHeights[i]<stack[-1][0]):
    stack.pop()
  index = None
  if(len(stack)==0):
    index=-1
  else:
    index = stack[-1][1]
  nsl.append(index)
  stack.append([buildingHeights[i],i])
maxArea = -1
for i in range(0,len(buildingHeights)):
  area = (nsr[i]-nsl[i]-1)*buildingHeights[i]
  maxArea = max(maxArea,area)
print(maxArea)