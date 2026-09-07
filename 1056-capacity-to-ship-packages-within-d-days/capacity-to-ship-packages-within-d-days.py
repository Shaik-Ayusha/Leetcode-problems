class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        n=len(weights)
        while l<=r:
            mid=(l+r)//2 
            summed=0 
            count=1
            for i in range(n):
                if summed+weights[i]>mid:
                    count+=1 
                    summed=weights[i]
                else:
                    summed+=weights[i]
            if count<=days:
                r=mid-1 
            else:
                l=mid+1 
        return l

        