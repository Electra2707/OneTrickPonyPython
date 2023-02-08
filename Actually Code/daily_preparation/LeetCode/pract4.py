class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = 0
        values = reversed([roman_dict[x] for x in s])

        return sum(values)


roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
print(Solution().romanToInt("III"))