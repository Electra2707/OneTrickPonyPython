"""Given a roman numeral, convert it to an integer.

:return: the program take a roman number and convert
it into an int
:rtype: int
"""

class Solution:
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        conversion = 0
        values = [Solution.roman_dict[x] for x in s]
        length_values = (len(values)-1)
        for i in range(length_values+1):
            num1 = values[i]
            if i == length_values:
                conversion = conversion + num1
                break
            num2 = values[i+1]
            if num1 >= num2:
                conversion = conversion + num1
            else:
                conversion = conversion - num1
        return conversion


print(Solution().romanToInt("MCMXCIV"))
