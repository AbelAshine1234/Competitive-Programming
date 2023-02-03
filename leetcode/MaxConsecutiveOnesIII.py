class Solution(object):
    def longestOnes(self, nums, k):
        i = 0
        for j in xrange(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1
