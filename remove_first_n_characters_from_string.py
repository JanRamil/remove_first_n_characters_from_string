# Remove first n characters from a string
# Exercise 4
# Creating a input code

# pseudocode

# Creating the input code for string
word = input("Please input your words here idol: ")

# Creating the code to get the number to be removed
num = int(input("Please enter the number of characters that you want to remove: "))

# Creating the print code for the output of the program
print("Removing the first", num, "characters from the string")

# Creating the remove string code 
new_word = word[num:]

# Creating the code for the outcome of the program
print("The original string is", word, "After removing characters, the new word is:", new_word)