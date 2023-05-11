'''
Create a program that replaces all connectives in a propositional formula
with only NOT, AND and OR without simplifying it.
'''

BOLD_TEXT_RED_BG = "\033[1;41m"
BOLD_TEXT_BLUE_BG = "\033[1;44m"
RESET_COLOR = "\033[0m"

OPEN_PAREN = "("
CLOSE_PAREN = ")"
NOT = "~"
AND = "^"
OR = "V"
COND = "->"
BICOND = "<->"


def findLeftSideStartIndex(formula: str, connectiveStartIndex: int) -> int:
   startIndex = connectiveStartIndex - 1

   # search for an opening parenthesis that has no matching closing parenthesis
   openParenCount = 0
   while ((startIndex > -1) and (openParenCount < 1)):
      if (formula[startIndex] == OPEN_PAREN):
         openParenCount += 1
      elif (formula[startIndex] == CLOSE_PAREN):
         openParenCount -= 1
      startIndex -= 1

   startIndex += 1
   if (openParenCount == 1):
      startIndex += 1

   return startIndex

def findRightSidePastEndIndex(formula: str, connectivePastEndIndex: int) -> int:
   pastEndIndex = connectivePastEndIndex

   # search for a closing parenthesis that has no matching opening parenthesis
   closeParenCount = 0
   while ((pastEndIndex < len(formula)) and (closeParenCount < 1)):
      if (formula[pastEndIndex] == CLOSE_PAREN):
         closeParenCount += 1
      elif (formula[pastEndIndex] == OPEN_PAREN):
         closeParenCount -= 1
      pastEndIndex += 1

   if (closeParenCount == 1):
      pastEndIndex -= 1

   return pastEndIndex


def replaceConnective(formula: str, connective: str, replaceFunc, printSteps: bool = True) -> str:
   while (connective in formula):
      connectiveStartIndex = formula.index(connective)
      if (printSteps):
         print(formula[:connectiveStartIndex] +
               BOLD_TEXT_RED_BG + connective + RESET_COLOR +
               formula[connectiveStartIndex + len(connective):])
      
      # find the start index of the proposition on the left side
      leftSideStartIndex = findLeftSideStartIndex(formula, connectiveStartIndex)
      # find the past end index of the proposition on the right side
      rightSidePastEndIndex = findRightSidePastEndIndex(formula, connectiveStartIndex + len(connective))

      formula = replaceFunc(formula,
                            leftSideStartIndex, connectiveStartIndex,
                            connectiveStartIndex + len(connective), rightSidePastEndIndex,
                            printSteps)

   return formula


def replaceBiconditional(formula: str, 
                         leftSideStartIndex: int, leftSidePastEndIndex: int,
                         rightSideStartIndex: int, rightSidePastEndIndex: int,
                         printChange: bool) -> str:
   # get all slices from the formula
   beforeLeftSide = formula[:leftSideStartIndex]
   leftSide = formula[leftSideStartIndex:leftSidePastEndIndex]
   rightSide = formula[rightSideStartIndex:rightSidePastEndIndex]
   afterRightSide = formula[rightSidePastEndIndex:]

   if (printChange):
      print(beforeLeftSide +
            BOLD_TEXT_BLUE_BG + OPEN_PAREN + OPEN_PAREN + RESET_COLOR +
            leftSide +
            BOLD_TEXT_BLUE_BG + CLOSE_PAREN + COND + OPEN_PAREN + RESET_COLOR +
            rightSide +
            BOLD_TEXT_BLUE_BG + CLOSE_PAREN + CLOSE_PAREN + AND + OPEN_PAREN + OPEN_PAREN + RESET_COLOR +
            rightSide +
            BOLD_TEXT_BLUE_BG + CLOSE_PAREN + COND + OPEN_PAREN + RESET_COLOR +
            leftSide +
            BOLD_TEXT_BLUE_BG + CLOSE_PAREN + CLOSE_PAREN + RESET_COLOR +
            afterRightSide +
            '\n')

   formula = (beforeLeftSide +
              OPEN_PAREN + OPEN_PAREN +
              leftSide +
              CLOSE_PAREN + COND + OPEN_PAREN +
              rightSide +
              CLOSE_PAREN + CLOSE_PAREN + AND + OPEN_PAREN + OPEN_PAREN +
              rightSide +
              CLOSE_PAREN + COND + OPEN_PAREN +
              leftSide +
              CLOSE_PAREN + CLOSE_PAREN + 
              afterRightSide)

   return formula


def replaceConditional(formula: str, 
                       leftSideStartIndex: int, leftSidePastEndIndex: int,
                       rightSideStartIndex: int, rightSidePastEndIndex: int,
                       printChange: bool) -> str:
   beforeLeftSide = formula[:leftSideStartIndex]
   leftSide = formula[leftSideStartIndex:leftSidePastEndIndex]
   rightSide = formula[rightSideStartIndex:rightSidePastEndIndex]
   afterRightSide = formula[rightSidePastEndIndex:]

   if (printChange):
      print(beforeLeftSide +
            BOLD_TEXT_BLUE_BG + NOT + OPEN_PAREN + RESET_COLOR +
            leftSide +
            BOLD_TEXT_BLUE_BG + CLOSE_PAREN + OR + OPEN_PAREN + RESET_COLOR +
            rightSide +
            BOLD_TEXT_BLUE_BG + CLOSE_PAREN + RESET_COLOR +
            afterRightSide +
            '\n')

   formula = (beforeLeftSide +
              NOT + OPEN_PAREN + 
              leftSide +
              CLOSE_PAREN + OR + OPEN_PAREN +
              rightSide +
              CLOSE_PAREN +
              afterRightSide)

   return formula

# "(r->(~p->q))->~p->(q->(s->q))"
formula = replaceConnective("(r<->(q<->s))", BICOND, replaceBiconditional)
replaceConnective(formula, COND, replaceConditional)
