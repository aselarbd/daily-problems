"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer
in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""


# Solution 1
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        distinct_nums = set(nums)
        count_map = {}

        for num in distinct_nums:
            count_map[num] = nums.count(num)

        counts = sorted(count_map.items(), key=lambda x: x[1], reverse=True)

        return [c[0] for c in counts[0:k]]


# solution 2
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
