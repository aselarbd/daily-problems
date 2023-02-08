"""
Given a string s, find the length of the longest
substring
 without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        subs = set()

        L, R = 0, 0

        while R < len(s):

            if L == R:
                subs.add(s[L])
                max_len = max(max_len, len(subs))
                R += 1
                continue

            if s[R] not in subs:
                subs.add(s[R])
            else:
                dup_idx = s[L:R + 1].find(s[R])
                L = dup_idx + L + 1
                subs = set([c for c in s[L:R + 1]])

            max_len = max(max_len, len(subs))
            R += 1

        return max_len
