# Write a program that defines a function called factorial that calculates the factorial of a number.
# The function should take a single argument, the number for which to calculate the factorial, and should
# return the result. The program should test the function by calling it with a few different numbers.

def factorial (n):
    result=1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(50))