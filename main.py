import random # Here, I imported "random".

minchoice = input("Enter the minimum number and press enter.")
# Print some text then wait for input.
maxchoice = float(input("Enter maximum number and press enter."))
# Print some text then wait for input.

num = random.randrange(int(minchoice), int(maxchoice)) # Set the number as the inputs.

print("The number is..") # Print "The number is..".
print(num) # Print the variable "num".
