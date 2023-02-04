# This script prompts the user to enter an email address and checks that the email address is in a valid format.
# To use the script, the user should enter their email address when prompted.

con=False  # variable used to control the while loop

while con == False:  # loop continues until the email address is found to be valid
    try:
        print("Write your email")
        email_Adress = input()  # get the email address from the user
        email_Adress = email_Adress.lower()  # convert the email address to lower case
        
        # check if the email address is in a valid format
        if not email_Adress or not email_Adress.strip() or "@" not in email_Adress or "." not in email_Adress:
            print("You didn't enter valid email. Please try again.")
        elif email_Adress[0] == "@" or email_Adress[-1] == "@":
            print("The email must contain at least one character before and after the "@" symbol. Please try again.")
        elif email_Adress[0] == "." or email_Adress[-1] == ".":
            print("The email must contain at least one character before and after the '.' symbol. Please try again.")
        elif "@." in email_Adress or "@ " in email_Adress or ".@" in email_Adress:
            print("The email cannot contain periods immediately before or after the "@" or '.' symbols. Please try again.")
        else:
            con = True  # set con to True to exit the while loop
    except Exception:  # catch any exceptions that may occur
        pass  # do nothing if an exception occurs
    
print(email_Adress)  # print the valid email address