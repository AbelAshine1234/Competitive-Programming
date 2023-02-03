class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(cardPoints):
            return sum(cardPoints)

        left,right,mini,tot = 0,0, sum(cardPoints), 0

        while right < len(cardPoints):
            while right - left + 1 <= len(cardPoints) - k:
                tot += cardPoints[right]
                if right - left + 1 == len(cardPoints) - k:
                    mini = min(tot,mini)
                right += 1

            while right - left + 1 > len(cardPoints) - k:
                tot -= cardPoints[left]
                left += 1

        return sum(cardPoints) - mini    
