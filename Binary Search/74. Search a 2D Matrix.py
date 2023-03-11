"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        L, R = 0, len(matrix) - 1

        while L <= R:
            M = (L + R) // 2

            if matrix[M][0] > target:
                R = M - 1
            elif matrix[M][-1] < target:
                L = M + 1
            else:
                if target in matrix[M]:
                    return True
                else:
                    return False
        return False
