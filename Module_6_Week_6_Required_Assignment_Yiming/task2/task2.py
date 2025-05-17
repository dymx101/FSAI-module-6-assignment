# 2. Conditional Statements (5 Marks) 

# Write a Python program that: 

# a) Prompts the user to enter a number. 

# b) Checks if the number is positive, negative, or zero. 

# c) Prints an appropriate message based on the result. 

number = int(input("Please input a number: "))
if number > 0:
    print("{number} is positive.".format(number = number))
elif number < 0:
    print("{0} is negative.".format(number))
else:
    print(number, "is zero.")