class Solution(object):
    def maxCoins(self, A):
        return sum(sorted(A)[len(A) / 3::2])
