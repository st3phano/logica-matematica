from connectives import *

BOLD_TEXT_RED_BG = "\033[1;41m"
BOLD_TEXT_BLUE_BG = "\033[1;44m"
RESET_COLOR = "\033[0m"

def findLeftSideStartIndex(formula: str, connectiveStartIndex: int) -> int:
   startIndex = connectiveStartIndex - 1

   # search for an opening parenthesis that has no matching closing parenthesis
   OPEN_PAREN = "("
   CLOSE_PAREN = ")"
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
   OPEN_PAREN = "("
   CLOSE_PAREN = ")"
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


def replaceConditional(formula: str, beforeLeftSide: str, leftSide: str,
                       rightSide: str, afterRightSide: str, printChange: bool) -> str:
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

def replaceBiconditional(formula: str, beforeLeftSide: str, leftSide: str,
                       rightSide: str, afterRightSide: str, printChange: bool) -> str:
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

def replaceConnective(formula: str, connective: str, printSteps: bool, replaceFunc) -> str:
   while (connective in formula):
      connectiveStartIndex = formula.index(connective)
      connectivePastEndIndex = connectiveStartIndex + len(connective)

      if (printSteps):
         print(formula[ : connectiveStartIndex] +
               BOLD_TEXT_RED_BG + connective + RESET_COLOR +
               formula[connectivePastEndIndex : ])

      leftSideStartIndex = findLeftSideStartIndex(formula, connectiveStartIndex)
      rightSidePastEndIndex = findRightSidePastEndIndex(formula, connectivePastEndIndex)
      
      beforeLeftSide = formula[ : leftSideStartIndex]
      leftSide = formula[leftSideStartIndex : connectiveStartIndex]
      rightSide = formula[connectivePastEndIndex : rightSidePastEndIndex]
      afterRightSide = formula[rightSidePastEndIndex : ]

      formula = replaceFunc(formula, beforeLeftSide, leftSide,
                            rightSide, afterRightSide, printSteps)

   return formula
