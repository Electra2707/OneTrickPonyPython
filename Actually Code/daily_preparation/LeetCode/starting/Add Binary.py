"""Add Binary
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result string and the carry bit
        result = ""
        carry = 0
        # Convert the strings to integers
        a = int(a, 2)
        b = int(b, 2)
        # Loop until both numbers are zero or there is a carry bit
        while a or b or carry:
            # Add the least significant bits of both numbers and the carry bit
            sum = (a & 1) + (b & 1) + carry
            # Append the least significant bit of the sum to the result string
            result = str(sum & 1) + result
            # Update the carry bit and right shift both numbers by one bit
            carry = sum >> 1
            a >>= 1
            b >>= 1
        # Return the result string
        return result


print(Solution().addBinary("11", "1"))
