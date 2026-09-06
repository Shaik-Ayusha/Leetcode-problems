class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        
        while l<=r:
           
            res=0
            mid=(l+r)//2 
            for pile in piles:
                res+=(pile+mid-1)//mid
                
            if res<=h:
                r=mid-1 
            else:
                l=mid+1 
        return l
            
        