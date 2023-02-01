"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""

from collections import deque


# solution 1
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero = deque()

        for n in nums:
            if n != 0:
                non_zero.appendleft(n)

        non_zero_count = len(non_zero)

        for i in range(len(nums)):
            if i < non_zero_count:
                nums[i] = non_zero.pop()
            else:
                nums[i] = 0


# Solution 2
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        L = 0

        for R in range(len(nums)):
            if nums[R]:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
