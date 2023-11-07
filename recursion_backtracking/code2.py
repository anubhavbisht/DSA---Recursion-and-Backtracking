# ---------------------------------------------------------------------------- #
#                              print abbreviations                             #
# ---------------------------------------------------------------------------- #
def printAbbreviations(string):
  if (len(string) == 0):
    return []
  else:
    firstChar = string[0]
    restOfString = string[1:]
    restOfStringAbbreviations = printAbbreviations(restOfString)
    totalCases = []
    if (len(restOfStringAbbreviations) == 0):
      totalCases.append(firstChar)
      totalCases.append('1')
    else:
      for i in restOfStringAbbreviations:
        totalCases.append(firstChar + i)
        firstCharacter = i[0]
        if (firstCharacter.isnumeric()):
          restOfString = i[1:]
          totalCases.append(str(int(firstCharacter) + 1) + restOfString)
        else:
          totalCases.append('1' + i)
    return totalCases

result = printAbbreviations('pep')
print(result, 'endddddddddd')