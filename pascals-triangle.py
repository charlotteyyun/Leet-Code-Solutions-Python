"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        # start off with the first two rows of the pascal's triangle
        ans = [[1], [1, 1]]
        # In Pascal's triangle, each number is the sum of the two numbers directly above it.
        for x in range(numRows - 2):
            l = [ans[-1][i] + ans[-1][i + 1] for i in range(x + 1)]
            ans.append([1] + l + [1])
        return ans
        """
        :type numRows: int
        :rtype: List[List[int]]
        """