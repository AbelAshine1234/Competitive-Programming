class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            n *= -1
            x = 1 / x
        elif not n:
            return 1
        half = self.myPow(x, n // 2)
        return x * half * half if n % 2 else half * half
