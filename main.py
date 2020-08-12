import random
# Import "random".

print("| Enter the minimum number and press enter.")
minnum = int(input())
# Print some text then wait for input, then set as variable and convert to integer.

print("| Enter maximum number and press enter.")
maxnum = int(input())
# Print some text then wait for input, then set as variable and convert to integer.

num = str(random.randrange(minnum, maxnum))
# Set the "num" variable to require random,
# to set the randrange from "minnum" to "maxnum" and convert to string.

print("| The number is "+ num +".")
# Print some text and attach the "num" variable.
