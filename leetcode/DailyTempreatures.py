class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        heap = []
        for j, t in enumerate(temperatures):
            while heap and heap[0][0] < t:
                temp, i = heapq.heappop(heap)
                res[i] = j - i
            heapq.heappush(heap, (t, j))
        return res
        
