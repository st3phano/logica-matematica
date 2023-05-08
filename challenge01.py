'''
Create a program that replaces all connectives in a propositional formula
with only NOT, AND and OR without simplifying it.
'''

RESET_COLOR = "\033[0m"

LEFT_PAREN = "("
RIGHT_PAREN = ")"
NOT_SIGN = "~"
AND_SIGN = "^"
OR_SIGN = "V"
COND_SIGN = "->"

def replaceConditionals(formula: str) -> str:
   colorValue = 1
   while (COND_SIGN in formula):
      index = formula.index(COND_SIGN)

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

      right = index + len(COND_SIGN)
      rightParenCount = 0
      while (right < len(formula) and rightParenCount < 1):
         if (formula[right] == RIGHT_PAREN):
            rightParenCount += 1
         elif (formula[right] == LEFT_PAREN):
            rightParenCount -= 1
         right += 1
      if (rightParenCount == 1):
         right -= 1

      color = f"\033[1;48;5;{colorValue}m"
      colorValue = (colorValue + 1) if (colorValue < 15) else 1
      formula = (formula[:left] +
                color + NOT_SIGN + LEFT_PAREN + RESET_COLOR +
                formula[left:index] +
                color + RIGHT_PAREN + OR_SIGN + LEFT_PAREN + RESET_COLOR +
                formula[(index + len(COND_SIGN)):right] +
                color + RIGHT_PAREN + RESET_COLOR +
                formula[right:])
      print(formula)

   return formula

replaceConditionals("r->(~p->q)->~p^q->(s->q)")
