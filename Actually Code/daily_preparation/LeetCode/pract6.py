"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def find_prefix(prefix: str, words: list[str]) -> bool:
            for element in words:
                if not prefix in element:
                    return False
            return True
        common_prefix = ""
        seen = set()
        queue = zip(strs, [1 for x in range(len(strs))])
        while queue:
            # for string in strs:
            #     prefix = string[:counter]
            #     if not prefix in seen:
            #         seen.add(prefix)
            element, counter = queue.pop(0)
            prefix = element[:counter]
            if prefix not in seen:
                
            if prefix in seen:
                continue
            if len(seen) == 2:
                common_prefix = prefix
                break
        return common_prefix


print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
