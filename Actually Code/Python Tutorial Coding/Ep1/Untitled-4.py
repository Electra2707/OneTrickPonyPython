# Prompt the user to enter a string
print("Write a string")

# Read the string from the user
var1 = (input())

# Convert the string to lowercase
var1 = var1.lower()

# Initialize a counter to track the number of vowels in the string
counter = 0

# List of vowels
vowels = ["a", "e", "i", "o", "u"]

# Iterate through each character in the string
for char in var1:
    
    # Check if the character is a vowel
    if char in vowels:
        
        # If it is a vowel, increment the counter
        counter += 1

# Print the results
print(f"In the word {var1} are {counter} of vowels")


# print("Write a string")
# var1=(input())
# num1=len(var1)
# counter=0
# vowels = ["a", "e", "i", "o", "u"]
# while len:
#     if var1 in vowels:
#         counter+=1

# print(f"In the word {var1} are {counter} of vowels")
