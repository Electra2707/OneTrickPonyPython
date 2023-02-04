def ask_word():
    while True:
        word=input("Write your word: ")
        if not word or not word.strip():
            print("Invalid input try again")
        else:
            return word

def ask_num():
    while True:
        try:
            num1=input("Write your integral number: ")
            if not num1.isnumeric() or not num1.strip():
                print("Invalid input, try again")
            else:
                return int(num1)
        except ValueError:
            print("Invalid input try again")

def ask_float():
    while True:
        try:
            fum1=input("Write your number: ")
            if not(not fum1.isdecimal() or fum1.isnumeric()) or not fum1.strip():
                print("Invalid input, try again")
            else:
                return float(fum1)
        except ValueError:
            print("Invalid input try again")

def factorial():
    n=ask_num()
    result=1
    for i in range(1,n+1):
        result *= i
    return result
