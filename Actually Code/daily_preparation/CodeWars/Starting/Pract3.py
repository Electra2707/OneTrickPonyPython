"""Write a function, persistence, that takes in a positive parameter num and
returns its multiplicative persistence, which is the number of times you must 
multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""


def persistence(number: int) -> int:
    number = abs(number)
    if number < 9:
        return 0
    digits = [int(d) for d in str(number)]
    result = 0
    while True:
        persisten = 1
        result += 1
        for i in digits:
            persisten *= i
        if persisten >= 0 and persisten <= 9:
            return result
        else:
            digits = [int(d) for d in str(persisten)]

    """The time complexity of the persistence function is O(n), 
    where n is the number of digits in the input number. 
    This is because the while loop runs until the number
    of digits is reduced to 1, and in each iteration, 
    it performs a constant number of operations (e.g. 
    conversion to list, product of digits and count 
    increment) regardless of the number of digits.
    """


print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))
