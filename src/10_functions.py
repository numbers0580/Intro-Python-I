# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(checknum):
    if checknum % 2 == 0:
        return "true"
    else:
        return "false"

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# I intentionally split up the obvious if-else statement into separate if-statements just to test out the 'not' logical operator
if is_even(num) is "true":
    print("Even!")

if is_even(num) is not "true":
    print("Odd")
