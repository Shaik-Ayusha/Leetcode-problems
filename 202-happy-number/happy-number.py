class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n>1 and n not in seen:
              seen.add(n)
              nums=n
          
              summed=0
              while nums>0:
                    summed+=(nums%10)*(nums%10)
                    nums=nums//10
              n=summed
            
        return n==1