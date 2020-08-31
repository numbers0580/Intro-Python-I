# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
print("I'm asked to print 2 to the 65536 power here.")
print ("Mathematician's Note: This will get ugly. 2^10 is ~1000, 2^20 is ~1 million, 2^30 is ~1 billion, etc.", "At that rate, we're expecting a value that has about 20,000 zeroes.")
print(f"Here goes: {2 ** 65536}")

print("Or another way:")
toobig = 2 ** 65536
print(toobig)