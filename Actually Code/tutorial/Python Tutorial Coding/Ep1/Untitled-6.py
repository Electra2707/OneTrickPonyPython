# Write a program that takes a string as input and replaces all occurrences of
# a certain letter with another letter.
import random
import string

# Set up a loop to ensure that the user enters a valid word
con = False
while con == False:
    try:
        # Prompt the user to enter a word
        print("Write a word")
        word = input()
        
        # Convert the word to lowercase
        word = word.lower()
        
        # Check if the user entered a valid word
        if not word or not word.strip() or not all(c in string.ascii_letters for c in word):
            # If not, print an error message and loop again
            print("You didn't enter a word. Please try again.")
        else:
            # If the user entered a valid word, exit the loop
            con = True
    except Exception:
        # Catch any errors and loop again
        pass

# List of replacement letters
replacement_letters = ["e", "t", "a", "i", "o", "n", "s", "h", "r"]

# Iterate through each character in the word
for char in word:
    
    # Choose a random replacement letter from the list
    random_letter = random.choice(replacement_letters)
    
    # Check if the character is in the list of replacement letters
    if char in replacement_letters:
        
        # If it is, replace the character with the random letter
        word = word.replace(char, random_letter)

# Print the modified word
print(word)

# print("Enter the letter you want to replace:")
# old_letter = input()
# print("Enter the replacement letter:")
# new_letter = input()

# modified_word = word.replace(old_letter, new_letter)

# print(modified_word)
