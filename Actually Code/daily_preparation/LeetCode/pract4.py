class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = 0
        for letter in s:
            value = roman_dict[letter]
            if value > conversion:
                conversion = conversion - value
            else:
                conversion = value
        return conversion


roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 100
}
print(Solution().romanToInt("LVIII"))