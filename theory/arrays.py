#-----------------------------------------------------------------------------
#
# Trivial example for arrays in Python3
#
#-----------------------------------------------------------------------------

# Let's make array in range 1 to 5 and simply print it
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Array -", array, end='\n\n')

# And we also can index it via []
print("Element at index 0:", array[0])
print("Element at index 1:", array[1])
print("Element at index 2:", array[2])
print("Element at index 3:", array[3])
print("Element at index 4:", array[4])
print("And other...", end='\n\n')

# Do it with cycle!
for i in array:
    print(i, end=' ')

print('\n')

# And we also can index it like this
print("array[0:3]:", array[0:3])
print("array[3:6]:", array[3:6])
print("array[6:9]:", array[6:9])
