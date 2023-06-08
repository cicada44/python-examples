#-----------------------------------------------------------------------------
#
# Trivial example for conditions in Python3
#
#-----------------------------------------------------------------------------

var = 5

# if var is more than 4, let's print that
if var > 4:
    print("var is more than 4!", end='\n\n')

# if var is less than 4, let's print that
if var < 4:
    print("var is less than 4!", end='\n\n')

anotherVar = 5

# if var equals to anotherVar, let's print that
if var == anotherVar:
    print("var equals to anotherVar", end='\n\n')

strVar1 = "one"
strVar2 = "two"

if strVar1 == strVar2:
    print("strVar1 equals to strVar2", end='\n\n')

if strVar2 == "two":
    print("strVar1 equals to 'two'", end='\n\n')
