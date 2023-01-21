class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        nums[::2], nums[1::2] = nums[n / 2:], nums[:n / 2]
        return nums
