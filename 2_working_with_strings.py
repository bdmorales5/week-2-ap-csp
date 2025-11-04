
# # ----------------------------------------
# # . Working with Strings
# # ----------------------------------------

# # Strings are sequences of characters enclosed in quotes (' ' or " ")
# greeting = "Hello"
# name = "World"

# # ----------------------------------------
# # Basic String Operations
# # ----------------------------------------

# # 1. Concatenation: Combining strings using the + operator
# message = greeting + " " + name
# print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
name= "BRANDON"

# Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!
print("lowercase name:", name.lower())


# Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
print("upercase name:",name.upper())
print("upercase name:",name.capitalize())

# Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("Is upercase?:",name.isupper())

# # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14

# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------
chicago_mayor="johnson"

print("first letter of mayor name:",chicago_mayor[0])
print("last letter of mayor name:",chicago_mayor[-1])
# # Indexing: Access characters by position (0-based index)
#get john
print("first four letters of mayors name:",chicago_mayor[0:4])
print("last three numbers for mayor name:",chicago_mayor[4:])
last_name= "morales"
print("last three characters in name:",last_name[4:])
# print("First character:", phrase[0])  # Output: P
poppins= "supercalifragilisticexpialidocious"
print("print out docios:",poppins[27:])
print("upercase:",poppins.upper())
print("print out super:",poppins[0:5])

declaration_of_indepedence="a decent respect for the opinions of mankind requires a people to explain the causes for their separation from another country"

# print("Last character:", phrase[-1])  # Output: !

# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!


# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

# sentence = "Python is fun to learn"

# .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)
words2=sentence.join("")

# .format(): Allows inserting values into strings using {}
name = "Marvin"
age = 35
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)

# You can also use f-strings (Python 3.6+)
intro_fstring = f"My name is {name} and I am {age} years old."
print(intro_fstring)
