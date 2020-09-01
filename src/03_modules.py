"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
if __name__ == "__main__":
    print("Current number of sys.argv:", len(sys.argv))
    for arg in sys.argv:
        print(arg)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("Windows details:", sys.getwindowsversion())
print("Windows", str(sys.getwindowsversion()[0]) + "." + str(sys.getwindowsversion()[1]), "build:", sys.getwindowsversion()[2])

# Print out the version of Python you're using:
# YOUR CODE HERE
print("Python details:", sys.version_info)
print("Python", str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2]), sys.version_info[3])


import os
import socket
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Process ID:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current Working Directory:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("Machine's Name", socket.gethostname())
# I found information for os.uname() that returns 5 tuple-like attributes, but...
# I keep getting the error: module 'os' has no attribute 'uname'