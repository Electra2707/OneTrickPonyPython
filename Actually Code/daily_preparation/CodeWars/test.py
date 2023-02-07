def its_sequential(number: int):
    string_number = str(number)
    return number % 10 == number and number //10 != 0


print(its_sequential(101))