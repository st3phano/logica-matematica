'''
Create a program that replaces all connectives in a propositional formula
with only NOT, AND and OR without simplifying it.
'''

import re
import connectives
from replace_connectives import replaceConnective
from replace_connectives import replaceBiconditional
from replace_connectives import replaceConditional

def main():
   formula = input("Type the desired formula:\n")
   
   # remove all white-space from the string
   WHITE_SPACE_REGEX = r"\s+"
   formula = re.sub(WHITE_SPACE_REGEX, "", formula) # (r->(~p<->q))->~p->(q->(s->q))
   print(f"{formula}\n")

   formula = replaceConnective(formula, connectives.BICOND, True, replaceBiconditional)
   formula = replaceConnective(formula, connectives.COND, True, replaceConditional)

   print(formula)

if __name__ == "__main__":
   main()
