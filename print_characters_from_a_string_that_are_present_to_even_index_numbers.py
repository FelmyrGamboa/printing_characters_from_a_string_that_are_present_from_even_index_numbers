# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# Expected Output:

# Orginal String is  pynative
# Printing only even index chars
# p
# n
# t
# v

# Ask user to input a string
input_string = str(input("Please type something: "))

print("Orginal String is", input_string)
print("Printing letters with even index number only")
# Create a for loop depending on the length of the string input
for i in range(0, len(input_string), 2):
# Display the result 