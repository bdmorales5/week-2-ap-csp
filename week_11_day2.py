# open up the vscode from previous day
# create a new file called: week11_day1.py
# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "brandon"
age = 15
favorite_color = "Blue"
favorite_number = 10

#  Step 2: Practice String Operations
# 1. Print your name in uppercase
print(first_name.upper())

# 2. Print how many letters are in your name
print(len(first_name))

# 3. Combine your name and favorite color into one message
print("My name is " + first_name + " and my favorite color is " + favorite_color + ".")

# Step 3: Math Practice
# Use arithmetic operators with your favorite number
print(favorite_number + 5)
print(favorite_number * 2)
print(favorite_number - 3)

# Step 4: User Input Practice
# Ask the user two questions and combine answers
hobby = input("What is your favorite hobby? ")
food = input("What is your favorite food? ")
print("You like " + hobby + " and enjoy eating " + food + ".")

# Step 5: Final Challenge (combine it all)
print(first_name + " is " + str(age) + " years old and likes the color " + favorite_color + 
      ". In 10 years, you will be " + str(age + 10) + " years old!")

