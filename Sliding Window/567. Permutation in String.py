"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.


Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Count = {}
        s2Count = {}

        for c in s1:
            s1Count[c] = 1 + s1Count.get(c, 0)

        L = 0

        for c in s2[0:len(s1)]:
            s2Count[c] = 1 + s2Count.get(c, 0)

        if s1Count == s2Count:
            return True

        for R in range(len(s1), len(s2)):
            s2Count[s2[L]] = s2Count[s2[L]] - 1

            if s2Count[s2[L]] <= 0:
                s2Count.pop(s2[L])

            L += 1
            s2Count[s2[R]] = 1 + s2Count.get(s2[R], 0)
            if s1Count == s2Count:
                return True

        return False
