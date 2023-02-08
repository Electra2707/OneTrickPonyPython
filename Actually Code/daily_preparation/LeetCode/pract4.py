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
