"""The task is to write a function is_interesting(number, awesome_phrases)
that returns 0, 1, or 2 based on whether the input number is an "interesting" number or not.

An "interesting" number is a 3-or-more digit number that meets one of the following criteria:

Any digit followed by all zeros: 100, 90000
Every digit is the same number: 1111
The digits are sequential, incrementing: 1234
The digits are sequential, decrementing: 4321
The digits are a palindrome: 1221 or 73837
The digits match one of the values in the awesome_phrases list
If an "interesting" number is within two miles of the input number, 
the function should return 1. If the input number is itself an "interesting"
number, the function should return 2. If neither of these criteria are met,
the function should return 0.

The input number will always be an integer greater than 0 and less than 
1,000,000,000. The awesome_phrases list will always be provided, and may be empty.
"""


