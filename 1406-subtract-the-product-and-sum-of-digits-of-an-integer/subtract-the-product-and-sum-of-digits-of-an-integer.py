class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        summed=0
        while n>0:
            digits=n%10 
            product=product*digits
            summed=summed+digits 
            n=n//10
        return product-summed
        
            


        