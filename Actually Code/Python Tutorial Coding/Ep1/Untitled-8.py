# This script takes a string as input and removes all punctuation from the string.
# To use the script, the user should enter a string when prompted.

# import the string module to access a list of punctuation characters
import string

# variable used to control the while loop
con = False

while con == False:
    print("Write something to remove the punctuation")
    word = input()
    
    # Check if the input is valid (not empty and contains at least one punctuation character)
    if not word or not word.strip() or not any(c in string.punctuation for c in word):
        print("Invalid input, Try again")
    else:
        con = True  # set con to True to exit the while loop

# Create a translation table that removes punctuation using the maketrans() method
trans_table = word.maketrans("", "", string.punctuation)

# Use the translate() method to remove the punctuation from the input string
word = word.translate(trans_table)

print(word)  # print the input string with the punctuation removed