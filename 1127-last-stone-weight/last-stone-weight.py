import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]
        for  stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap)>1:
            first=-heapq.heappop(heap)
            second=-heapq.heappop(heap)
            if first==second:
                continue 
            else:
                diff=abs(first-second)
                heapq.heappush(heap,-diff)
        if heap:
            return -heap[0]
        return 0

        