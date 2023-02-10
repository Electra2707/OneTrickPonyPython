"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from collections import deque


class Solution:
    # def longestCommonPrefix(self, strs):
    #     if not strs:
    #         return ""
    #     prefix = min(strs, key=len)
    #     for i, char in enumerate(prefix):
    #         for word in strs:
    #             if word[i] != char:
    #                 return prefix[:i]
    #     return prefix

    def longestCommonPrefix(self, strs: list[str]) -> str:
        def find_prefix(prefix: str, words: list[str]) -> bool:
            for element in words:
                if not prefix in element:
                    return False
            return True
        common_prefix = ""
        seen = set()
        queue = deque(zip(strs, [1 for x in range(len(strs))]))
        while queue:
            element, counter = queue.popleft()
            prefix = element[:counter]
            if not element or len(prefix) >= len(element):
                break
            if prefix not in seen:
                if find_prefix(prefix, strs):
                    counter += 1
                    common_prefix = prefix
                    seen.add(prefix)
                    queue.append((element, counter))
                else:
                    break
            else:
                continue
        return common_prefix


print(Solution().longestCommonPrefix(["a"]))
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
