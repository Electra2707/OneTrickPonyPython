#Write a program that asks the user for a year, and then prints "Leap year" if
#the year is a leap year, and "Regular year" if it is not a leap year. A leap year
#is a year that is divisible by 4, except for years that are divisible by 100 but 
#not by 400. For example, 2000 is a leap year, but 1900 is not.

# print("Select your year")
# year=int(input())
# Exception=False

# def calculation():
#     if year%100==0 and not year%400:
#         Exception=True

# if (year%4==0) and Exception==True:
#     print("Leap Year")
# else:
#     print("Regular Year")

# Print a prompt for the user to select a year
print("Select your year")

# Get the year from the user's input
year = int(input())

def calculation(year):
    # Check if the year is a leap year
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and not (year % 100 == 0):
        return True
    else:
        return False
    
# Calculate whether the year is a leap year
leap_year = calculation(year)

# Print the result
if leap_year:
    print("Leap Year")
else:
    print("Regular year")