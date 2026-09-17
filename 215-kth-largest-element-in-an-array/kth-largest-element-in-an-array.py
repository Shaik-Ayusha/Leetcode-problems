import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap=[]
        for num in nums:
            heapq.heappush(heap,-num)
        while k>0:
            res=heapq.heappop(heap)
            k=k-1 
        return -res
        