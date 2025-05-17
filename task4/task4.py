# 4. Functions (5 Marks)

# Write a program that: 

# a) Defines a function to calculate the area of a rectangle using length and width as inputs. 

# b) Prompts the user to input values for length and width. 

# c) Calls the function to calculate and then displays the area in a formatted message. 

def calculateArea(length, width):
    return length * width

print("Let me help you to calculate the area of a rectangle.")
length = float(input("Please input the length: "))
width = float(input("Please input the width: "))
area = calculateArea(length, width)

print("The area of rectangle (length: {length}, width: {width}) is {area}.".format(length = length, width = width, area = area))