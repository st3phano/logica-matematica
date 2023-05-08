'''
Create a program that replaces all connectives in a propositional formula
with only NOT, AND and OR without simplifying it.
'''
BOLD_TEXT_RED_BG = "\033[1;41m"
BOLD_TEXT_BLUE_BG = "\033[1;44m"
RESET_COLOR = "\033[0m"

LEFT_PAREN = "("
RIGHT_PAREN = ")"
NOT = "~"
AND = "^"
OR = "V"
COND = "->"
BICOND = "<->"

def replaceBiconditionals(formula: str, printSteps = True) -> str:
   while (BICOND in formula):
      index = formula.index(BICOND)
      if (printSteps):
         print(formula[:index] + BOLD_TEXT_RED_BG + BICOND + RESET_COLOR + formula[(index + len(BICOND)):])
      
      left = index - 1
      leftParenCount = 0
      while (left > 0 and leftParenCount < 1):
         if (formula[left] == LEFT_PAREN):
            leftParenCount += 1
         elif (formula[left] == RIGHT_PAREN):
            leftParenCount -= 1
         left -= 1
      if (leftParenCount == 1):
         left += 2

      right = index + len(BICOND)
      rightParenCount = 0
      while (right < len(formula) and rightParenCount < 1):
         if (formula[right] == RIGHT_PAREN):
            rightParenCount += 1
         elif (formula[right] == LEFT_PAREN):
            rightParenCount -= 1
         right += 1
      if (rightParenCount == 1):
         right -= 1

def replaceConditionals(formula: str, printSteps = True) -> str:
   while (COND in formula):
      index = formula.index(COND)
      if (printSteps):
         print(formula[:index] + BOLD_TEXT_RED_BG + COND + RESET_COLOR + formula[(index + len(COND)):])

      left = index - 1
      leftParenCount = 0
      while (left > 0 and leftParenCount < 1):
         if (formula[left] == LEFT_PAREN):
            leftParenCount += 1
         elif (formula[left] == RIGHT_PAREN):
            leftParenCount -= 1
         left -= 1
      if (leftParenCount == 1):
         left += 2

      right = index + len(COND)
      rightParenCount = 0
      while (right < len(formula) and rightParenCount < 1):
         if (formula[right] == RIGHT_PAREN):
            rightParenCount += 1
         elif (formula[right] == LEFT_PAREN):
            rightParenCount -= 1
         right += 1
      if (rightParenCount == 1):
         right -= 1

      if (printSteps):
         print(formula[:left] +
               BOLD_TEXT_BLUE_BG + NOT + LEFT_PAREN + RESET_COLOR +
               formula[left:index] +
               BOLD_TEXT_BLUE_BG + RIGHT_PAREN + OR + LEFT_PAREN + RESET_COLOR +
               formula[(index + len(COND)):right] +
               BOLD_TEXT_BLUE_BG + RIGHT_PAREN + RESET_COLOR +
               formula[right:])

      formula = (formula[:left] +
                 NOT + LEFT_PAREN + formula[left:index] + RIGHT_PAREN +
                 OR +
                 LEFT_PAREN + formula[(index + len(COND)):right] + RIGHT_PAREN +
                 formula[right:])

   return formula

replaceConditionals("r->(~p->q)->~p^(q->(s->q))")
