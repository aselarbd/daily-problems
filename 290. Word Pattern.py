"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        pattern_map = {}
        mapped_words = []

        if len(pattern) != len(s.split(' ')):
            return False

        for i, (p, word) in enumerate(zip(list(pattern), s.split(' '))):
            if p not in pattern_map:
                if word not in mapped_words:
                    pattern_map[p] = word
                    mapped_words.append(word)
                else:
                    return False
            else:
                if word != pattern_map[p]:
                    return False

        return True
