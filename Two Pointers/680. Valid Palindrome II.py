"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.


Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        L, R = 0, len(s) - 1

        while L < R:

            if s[L] != s[R]:
                left_skip = s[L + 1:R + 1]
                right_skip = s[L:R]

                return left_skip == left_skip[::-1] or right_skip == right_skip[::-1]

            L += 1
            R -= 1
        return True
