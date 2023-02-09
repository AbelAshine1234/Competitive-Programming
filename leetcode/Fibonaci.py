class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.fib(n - 1) + self.fib(n - 2) if n > 1 else n

