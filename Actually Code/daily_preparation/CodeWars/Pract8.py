"""This exercise is asking you to write a function 
called productFib(prod) that takes in an integer prod and returns an array.
The array should contain three elements: two Fibonacci numbers F(n) and F(n+1),
and a boolean value that is true if F(n) * F(n+1) = prod and false otherwise.
The Fibonacci sequence is a sequence of numbers in which each number is the sum 
of the two preceding ones, usually starting with 0 and 1.

In this problem, you need to find the two Fibonacci numbers F(n) and 
F(n+1) such that their product is equal to the input number prod. 
If there is such pair of numbers, you should return 
[F(n), F(n+1), true]. If there is no such pair of numbers and the 
product of F(n) and F(n+1) is less than the input number prod, you
should return [F(n), F(n+1), false].

For example, if the input number is 714, the function should return
[21, 34, true] because 21 * 34 = 714. If the input number is 800, 
the function should return [34, 55, false] because 21 * 34 < 800 < 34 * 55."""


def productFib(prod: int):
    # Initialize the first two numbers in the Fibonacci sequence
    num1 = 0
    num2 = 1
    # Iterate through the range of the input number
    for _ in range(prod):
        # Check if the product of the current numbers is greater than or equal to the input number
        if num1*num2 >= prod:
            # If it is, exit the loop
            break
        else:
            # If not, update the Fibonacci sequence by shifting the values
            old_num1 = num1
            num1 = num2
            num2 = old_num1 + num1
    # Return the last two numbers in the Fibonacci sequence and a boolean value indicating if the product is equal to the input
    return [num1, num2, num1*num2 == prod]

def productFib(prod):
    a,b = 0,1
    while a*b < prod:
        a,b = b, b+a
    return [a, b, a*b == prod]

print(productFib(4895))  # , [55, 89, True])
print(productFib(5895))  # , [89, 144, False])
