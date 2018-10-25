"""Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7]."""

class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        digits = ""
        s = num / abs(num)
        num = abs(num)
        while num:
            digits += str(int(num % 7))
            num //= 7
        return str(int(digits[::-1]) * s)
        """
        :type num: int
        :rtype: str
        """
