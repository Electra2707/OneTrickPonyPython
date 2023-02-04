# Write a Python script to rename all the files in a directory. The script should take the directory name as input and rename all the files
# by adding a prefix to the existing file name.

# Import the necessary modules
import os
import subprocess
import time

# Function to get the directory name from the user and validate it
def ask_input():
    # Loop until a valid directory is entered
    while True:
        # Clear the screen
        subprocess.run("cls", shell=True)
        # Get the directory name from the user
        directory = input(
            "Write your dir to rename the files add them and index\n")
        # Check if the entered directory is valid
        if os.path.isdir(directory):
            print("Directory accepted")
            print(os.listdir(directory))
            # Get the user's confirmation to proceed
            confirmation = input("Continue? S/N: ")
            # If the user confirms, break out of the loop
            if confirmation.upper() == "S":
                break
        # If the directory is not valid, print an error message and try again
        print("Wrong input try again")
        time.sleep(0.5)
    # Return the directory name
    return directory

# Function to get the starting index from the user
def ask_num():
    # Loop until a valid index is entered
    while True:
        # Clear the screen
        subprocess.run("cls", shell=True)
        # Get the starting index from the user
        num1 = input("Add your starting number: ")
        # Check if the index is a valid number
        if not num1.isnumeric() or not num1.strip():
            # If the index is not a valid number, print an error message and try again
            print("Invalid input, try again")
            time.sleep(0.5)
        else:
            # If the index is valid, convert it to an integer and return it
            return int(num1)
            break

# Get the directory name from the user
directory = ask_input()
# Clear the screen
subprocess.run("cls", shell=True)
# Print the default index format
print("The default rename index will be (1 example_file)")
# Get the user's input on whether they want to specify a custom index
index_confirmation = input("Do you want any particular index? S/N: ")
# Set the default separator to a space character
espace = " "
# Set the default index number to 0
index_number=1
# List of characters that are not allowed in file names on Windows
invalid_espace = ("\\", "/", ":", "*", "?", '"', "<", ">", "|")
# If the user wants to specify a custom index
if index_confirmation.upper() == "S":
    # Clear the screen
    subprocess.run("cls", shell=True)
    # Get the starting index from the user
    index_number = ask_num()
# Get the character that should be used to separate the index and the file name
    while True:
        espace = input("Add the connection between the number and the file: ")
        # Check if the character is allowed by Windows
        if not espace in invalid_espace:
            break
        else:
            print(
                f"Windows don't allow to name files like {invalid_espace}, try again")

# Try to rename the files
try:
    # Get the list of files in the directory
    files = os.listdir(directory)
    # Iterate through the list of files
    for i, file in enumerate(files):
        # Rename the file by adding the index and the separator character
        os.rename(os.path.join(directory, file), os.path.join(
            directory, str(index_number+i) + espace + file))
    # Print a success message
    print("Files successfully renamed")
    # Print the list of renamed files
    print(os.listdir(directory))
        # Wait 2 seconds before asking for the directory again
    time.sleep(2)
# Catch any permissions errors that might occur
except PermissionError as error:
    # Clear the screen and print the error message
    subprocess.run("cls", shell=True)
    print(error)
    print("Try again")
    # Wait 2 seconds before asking for the directory again
    time.sleep(2)
    directory = ask_input()