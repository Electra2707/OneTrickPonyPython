"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""
        seen = set()
        for i in range(len(strs)):
            prefix = strs[i][:i+1]
            if not prefix in seen:
                seen.add(prefix)
        while strs:
            element = strs.pop(0)
            if len(seen) == 2:
                common_prefix = prefix
                break
            strs.append(element)
        return common_prefix


print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
