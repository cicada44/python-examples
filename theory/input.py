#-----------------------------------------------------------------------------
#
# Trivial example for input process in Python3
#
#-----------------------------------------------------------------------------

# Let's input smt
var = input()
print("var -", var, end='\n\n')

# But...
# var = var + 5
# print("var -", var, end='\n\n')

# Let's do it again using int()
var = int(input())
var = var + 5
print("var -", var, end='\n\n')

# And another axample
stringVar = input()
stringVar = stringVar + "ending"
print("strinVar -", stringVar, end='\n\n')

# Difficult
listVar = list(input("Input list: "))
print("listVar -", listVar, end='\n\n')
