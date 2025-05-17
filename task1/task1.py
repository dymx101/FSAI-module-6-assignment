# 1. Variables and Data Types (5 Marks) 

# Write a Python program that: 

# a) Declares variables for storing a user’s name, age, and height. 

# b) Prints a greeting message using the name. 

# c) Calculates the user’s age 10 years from now. 

# d) Displays height in meters by converting height from centimetres. 

name = "Mike"
age = 30
height = 185.0
print("Hello, {}!".format(name))
ageAfterTenYears = age + 10
print("You will be", ageAfterTenYears, "years old after 10 years.")
print("Your height is {:.2f} meters".format(height/100))