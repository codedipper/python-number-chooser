import random
# Import "random".

minchoice = input("Enter the minimum number and press enter.")
# Print some text then wait for input, then set as variable.
maxchoice = input("Enter maximum number and press enter.")
# Print some text then wait for input, then set as variable.

minnum = int(minchoice)
# Create variable "minnum" as the integer of "minchoice".
maxnum = int(maxchoice) + 1
# Add 1 to the pre-stated "maxchoice" variable (to fix bugs).

num = random.randrange(minnum, maxnum)
# Set the "num" variable to require random,
# to set the randrange from "minnum" to "maxnum".

print("The number is..")
# Print some text.

print(num)
# Print the variable "num".
