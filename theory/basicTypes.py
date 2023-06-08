#-----------------------------------------------------------------------------
#
# Trivial example for basic types in Python3
#
#-----------------------------------------------------------------------------

# Variable has type 'integer' (целое число)
intVar = 5
print("type of 'intVar' -", type(intVar), end='\n\n')

# We've already seen that...

# Var has type 'string'
var = input("Input var: ")
print("type of 'var' -", type(var), end='\n\n')

# Var has type 'integer'!
var = int(input("Input var: "))
print("type of 'var' -", type(var), end='\n\n')

# Type 'float' (число с плавающей точкой)
floatVar = float(input("Input floatVar: "))
print("floatVar -", floatVar)
print("type of floatVar -", floatVar, end='\n\n')

# Type 'list'
listVar = list(input("Input list: "))
print("listVar -", listVar)
print("type of listVar -", type(listVar))
