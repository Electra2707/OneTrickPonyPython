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
        new_values = [-1] + values
        for num1, num2 in zip(values, new_values):
            if num1 == num2:
                conversion = conversion + num1
            elif num1>num2:
                conversion = conversion + num1
            elif num1<num2:
                conversion = conversion - num1
        return conversion


print(Solution().romanToInt("LVIII"))
