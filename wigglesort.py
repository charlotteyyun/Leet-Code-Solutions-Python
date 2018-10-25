"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
"""
class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1
        nums[::2], nums[1::2] = nums[:n][::-1], nums[n:][::-1]

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """