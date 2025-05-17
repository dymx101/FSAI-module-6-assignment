# 3. Loops and Iteration (5 Marks) 

# Write a program that: 

# a) Prompts the user to input an integer nnn. 

# b) Uses a for loop to print all even numbers from 1 up to nnn. 

# c) Ensures only even numbers appear in the output.

nnn = int(input("Please input a number: "))
print("All even numbers from 1 to {} are listed here:".format(nnn))
# Since 1 is odd number, we start from 2 which is even.
for number in range(2, nnn + 1, 2):
    print(number)
