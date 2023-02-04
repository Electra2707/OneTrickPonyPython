# Write a program that takes a string as input and converts it to title case # (i.e., all words should start with a capital letter).

def to_title_case(s):
    # check if input is valid
    if not s or not s.strip():
        return "Invalid input"

    # convert string to title case
    return s.title()

while True:
    print("Write a sentence:")
    s = input()
    # exit loop if input is empty
    if not s:
        break

    print(to_title_case(s))

# WLop=False
# while WLop==False:
#     print("Write a sentence")
#     Word=input()
#     if not Word or not Word.strip() or Word.isalnum():
#         print("Invalid input")
#     else:
#         Word = Word.title()
#         print(Word)
#         WLop = True