"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []

        for i in range(numRows):

            if i == 0:
                res.append([1])
            elif i == 1:
                res.append([1, 1])
            else:
                r = res[i - 1]
                temp = []

                for j in range(len(r) - 1):
                    temp.append(r[j] + r[j + 1])

                temp.insert(len(temp), 1)
                temp.insert(0, 1)

                res.append(temp)

        return res
