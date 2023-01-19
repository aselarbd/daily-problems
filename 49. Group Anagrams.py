"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [strs]

        sorted_list = ["".join(sorted(ana)) for ana in strs]
        group_map = {}

        for i, word in enumerate(sorted_list):
            if word not in group_map:
                group_map[word] = [i]
            else:
                group_map[word].append(i)

        res = []

        for k in group_map:
            res.append([strs[idx] for idx in group_map[k]])

        return res
