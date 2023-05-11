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

def replaceBiconditionals(formula: str, printSteps: bool = True) -> str:
   while (BICOND in formula):
      index = formula.index(BICOND)
      if (printSteps):
         print(formula[:index] + BOLD_TEXT_RED_BG + BICOND + RESET_COLOR + formula[(index + len(BICOND)):])
      
      left = index - 1
      leftParenCount = 0
      while (left > 0 and leftParenCount < 1):
         if (formula[left] == OPEN_PAREN):
            leftParenCount += 1
         elif (formula[left] == CLOSE_PAREN):
            leftParenCount -= 1
         left -= 1
      if (leftParenCount == 1):
         left += 2

      right = index + len(BICOND)
      rightParenCount = 0
      while (right < len(formula) and rightParenCount < 1):
         if (formula[right] == CLOSE_PAREN):
            rightParenCount += 1
         elif (formula[right] == OPEN_PAREN):
            rightParenCount -= 1
         right += 1
      if (rightParenCount == 1):
         right -= 1

def replaceConditionals(formula: str, printSteps: bool = True) -> str:
   while (COND in formula):
      index = formula.index(COND)
      if (printSteps):
         print(formula[:index] + BOLD_TEXT_RED_BG + COND + RESET_COLOR + formula[(index + len(COND)):])

      left = index - 1
      openParenCount = 0
      while ((left > 0) and (openParenCount < 1)):
         if (formula[left] == OPEN_PAREN):
            openParenCount += 1
         elif (formula[left] == CLOSE_PAREN):
            openParenCount -= 1
         left -= 1
      if (openParenCount == 1):
         left += 2

      right = index + len(COND)
      closeParenCount = 0
      while ((right < (len(formula) - 1)) and (closeParenCount < 1)):
         if (formula[right] == CLOSE_PAREN):
            closeParenCount += 1
         elif (formula[right] == OPEN_PAREN):
            closeParenCount -= 1
         right += 1
      if (closeParenCount == 1):
         right -= 2

      if (printSteps):
         print(formula[:left] +
               BOLD_TEXT_BLUE_BG + NOT + OPEN_PAREN + RESET_COLOR +
               formula[left:index] +
               BOLD_TEXT_BLUE_BG + CLOSE_PAREN + OR + OPEN_PAREN + RESET_COLOR +
               formula[(index + len(COND)):right] +
               BOLD_TEXT_BLUE_BG + CLOSE_PAREN + RESET_COLOR +
               formula[right:])
         print()

      formula = (formula[:left] +
                 NOT + OPEN_PAREN + formula[left:index] + CLOSE_PAREN +
                 OR +
                 OPEN_PAREN + formula[(index + len(COND)):(right + 1)] + CLOSE_PAREN +
                 formula[right + 1:])

   return formula

replaceConditionals("r->(~p->q)->~p^(q->(s->q))")
