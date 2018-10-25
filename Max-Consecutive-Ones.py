"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        l = []
        for num in nums:
            if num ==1:
                count += 1
            else:
                l.append(count)
                count = 0
        l.append(count)
        return (max(l))
        """
        :type nums: List[int]
        :rtype: int
        """