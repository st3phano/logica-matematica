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
   print("Logical connectives symbols:")
   print(f"[-] not: {connectives.NOT}")
   print(f"[-] and: {connectives.AND}")
   print(f"[-] or: {connectives.OR}")
   print(f"[-] conditional: {connectives.COND}")
   print(f"[-] biconditional: {connectives.BICOND}")
   formula = input("Type the desired formula:\n")
   
   # remove all white-space from the string
   WHITE_SPACE_REGEX = r"\s+"
   formula = re.sub(WHITE_SPACE_REGEX, "", formula)
   print(f"\nFormula without white-space:\n{formula}\n")

   printSteps = True;
   if (printSteps):
      print("Steps:")
   formula = replaceConnective(formula, connectives.BICOND, printSteps, replaceBiconditional)
   formula = replaceConnective(formula, connectives.COND, printSteps, replaceConditional)

   print(f"Formula with only NOT, AND and OR:\n{formula}")

if __name__ == "__main__":
   main()
