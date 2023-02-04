# This script prompts the user to enter their age and then determines if they are a minor or an adult.
# To use the script, the user should enter their age when prompted.

print("Insert your age")
age = int(input())  # get the age from the user

# check if the age is a minor or an adult
if age < 18 and age > -1:  # age must be greater than or equal to 0 and less than 18
    print("Minor")
elif age >= 18:  # age must be greater than or equal to 18
    print("Adult")
else:  # age is less than 0 or greater than 120
    print("Invalid age")
