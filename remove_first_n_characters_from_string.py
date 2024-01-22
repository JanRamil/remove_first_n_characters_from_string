# Remove first n characters from a string
# Exercise 4

# pseudocode

# Creating the starting code including the def remove_first_n_characters_from_string
def remove_first_n_characters_from_string(input_string, n):
    if n >= 0:
        return input_string[n:]
    else:
        return "Error: Please provide a non-negative value for n."
