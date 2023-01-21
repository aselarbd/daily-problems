"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

import string


# Solution 1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        alphabet = list(string.printable)

        s_i = 0
        t_i = 0
        for i, (s_l, t_l) in enumerate(zip(s, t)):
            if s_l in s_map:
                s = s[:i] + s_map[s_l] + s[i + 1:]
            else:
                s_map[s_l] = alphabet[s_i]
                s = s[:i] + alphabet[s_i] + s[i + 1:]
                s_i += 1

            if t_l in t_map:
                t = t[:i] + t_map[t_l] + t[i + 1:]
            else:
                t_map[t_l] = alphabet[t_i]
                t = t[:i] + alphabet[t_i] + t[i + 1:]
                t_i += 1

        if s == t:
            return True
        else:
            return False


# Solution 2
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(zip(s, t))) == len(set(t))
