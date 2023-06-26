"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        def find_common_pattern(str1, str2):
            common_pattern = ""
            for char1, char2 in zip(str1, str2):
                if char1 == char2:
                    common_pattern += char1
                else:
                    break
            return common_pattern

        pattern = find_common_pattern(strs[0], strs[1])

        if pattern == "":
            return ""
        else:
            for word in strs[1:]:
                pattern = find_common_pattern(pattern, word)

            return pattern
