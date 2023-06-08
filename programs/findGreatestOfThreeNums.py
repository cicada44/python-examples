#-----------------------------------------------------------------------------
#
# Greatest of 3 inputted numbers in Python3
#
#-----------------------------------------------------------------------------

n1 = int(input("Input n1: "))
n2 = int(input("Input n2: "))
n3 = int(input("Input n3: "))

if (n1 >= n2) and (n1 >= n3):
    greatest = n1
elif (n2 >= n1) and (n2 >= n3):
    greatest = n2
else:
    greatest = n3

print("greatest:", greatest)

# Maybe that's not so difficult...
