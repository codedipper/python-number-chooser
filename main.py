import random
# Import "random".

print("[System]: | Enter the minimum number and press enter.\n")
minnum = int(input("[You]: | "))
# Print some text then wait for input, then set as variable and convert to integer.

print("\n[System]: | Enter maximum number and press enter.\n")
maxnum = int(input("[You]: | "))
# Print some text then wait for input, then set as variable and convert to integer.

num = random.randint(minnum, maxnum)
# Set the "num" variable to require random.
# And set the randint from "minnum" to "maxnum".

print("\n[System]: | The number is '", num ,"'.\n")
# Print some text and attach the "num" variable.

