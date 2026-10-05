from collections import deque
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxdeque=deque()
        mindeque=deque()
        l=0
        r=0 
        max_len=0
        n=len(nums)
        while r<n:
            while maxdeque and nums[maxdeque[-1]]<nums[r]:
                maxdeque.pop()
            maxdeque.append(r)
            while mindeque and nums[mindeque[-1]]>nums[r]:
                mindeque.pop()
            mindeque.append(r)
            while nums[maxdeque[0]]-nums[mindeque[0]]>limit:
                if maxdeque[0]==l:
                    maxdeque.popleft()
                    
                if mindeque[0]==l:
                    mindeque.popleft()
                l+=1 
                
            max_len=max(max_len,r-l+1)
            r+=1
        return max_len

        