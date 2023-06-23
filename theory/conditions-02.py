#-----------------------------------------------------------------------------
#
# Trivial example for conditions in Python3
#
#-----------------------------------------------------------------------------

x = 1
y = 2
z = 3

if x < y and y < z:
    print("x less than y and y less than z", end='\n\n')

if x < y or y > z:
    print("x less than y or z less than y", end='\n\n')

if x < y:
    print("x less than y")
else:
    print("x greater or equal than y")

if x > y:
    print("x greater than y")
else:
    print("x less than y")

j = 1

if j == z:
    print("j equals to z")
elif j == y:
    print("j equals to y")
elif j == x:
    print("j equals to x")

