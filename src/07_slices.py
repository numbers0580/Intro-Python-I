"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1:2])

# Output the second-to-last element: 9
print(a[len(a) - 2:len(a) - 1]) # this is effectively print(a[4]), but written for any length of array of at least size 2

# Output the last three elements in the array: [7, 9, 6]
print(a[len(a) - 3:]) # this is effectively print(a[3:]), but I wrote the code for all possible sizes of arrays of at least 3

# Output the two middle elements in the array: [1, 7]
print(a[2:4]) # In this case, I did not write the code for all cases, since the math varies for even and odd-length arrays, and I didn't want to get into that, yet.

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:]) # This works already for all cases for arrays of at least size 2

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:len(a) - 1]) # This is effectively print(a[:5]), but written for all cases, regardless of array size

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])