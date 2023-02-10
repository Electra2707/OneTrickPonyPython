"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""


# def longestCommonPrefix(self, strs):
#     if not strs:
#         return ""
#     prefix = min(strs, key=len)
#     for i, char in enumerate(prefix):
#         for word in strs:
#             if word[i] != char:
#                 return prefix[:i]
#     return prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) <= 1:
            return strs[0]

        common_prefix = ""
        seen = set()
        queue = [(strs, 1)]
        while queue:
            elements, counter = queue.pop(0)
            prefix = elements[0][:counter]
            if not elements[0] or len(prefix) > len(elements[0]):
                break
            if prefix not in seen:
                if all(element.startswith(prefix) for element in elements):
                    counter += 1
                    common_prefix = prefix
                    seen.add(prefix)
                    queue.append((elements, counter))
                else:
                    break
        return common_prefix
# from collections import deque
        # if len(strs) <= 1:
        #     return strs[0]

        # def find_prefix(prefix: str, words: list[str]) -> bool:
        #     for element in words:
        #         element = element[:len(prefix)]
        #         if not prefix == element:
        #             return False
        #     return True
        # common_prefix = ""
        # seen = set()
        # queue = deque(zip(strs, [1 for x in range(len(strs))]))
        # while queue:
        #     element, counter = queue.popleft()
        #     prefix = element[:counter]
        #     if not element or len(prefix) > len(element):
        #         break
        #     if prefix not in seen:
        #         if find_prefix(prefix, strs):
        #             counter += 1
        #             common_prefix = prefix
        #             seen.add(prefix)
        #             queue.append((element, counter))
        #         else:
        #             break
        #     else:
        #         continue
        # return common_prefix


print(Solution().longestCommonPrefix(["c", "acc", "ccc"]))
print(Solution().longestCommonPrefix(["flower", "flower", "flower", "flower"]))
