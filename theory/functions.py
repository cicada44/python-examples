#-----------------------------------------------------------------------------
#
# Trivial example for functions in Python3
#
#-----------------------------------------------------------------------------

# Make out first function
def useless(something):
    return something

n = 5;
print("n:", n, end='\n\n')

# Let's make function that returns absolute number
def abs(number):
    # If number less than 0, multiply it on -1
    if number < 0:
        number *= -1
    
    # Return it
    return number

# Create negative number and make it postitive, then print it
n = -100
n = abs(n)
print("n:", n, end='\n\n')

# And fuction that return max number in list
def max(list):
    # Max element is the first
    maximum = list[0]

    # And detect the real maximum number 
    for i in list:
        # If current number is more than actual maximum - replace it
        if i > maximum:
            maximum = i

    # Return it
    return maximum

# Make list
l = (1, 2, 3, 4, 5, 5, 4, 3, 2, 1)

# Call our max function
m = max(l)

# Print result
print("max of list:", m)


