class Solution:
    def maxProduct(self, n: int) -> int:
        f_m=0
        s_m=0
        while n!=0:
            digits=n%10
            if digits>f_m:
                s_m=f_m 
                f_m=digits
            elif digits>s_m:
                s_m=digits
            n=n//10
        return s_m*f_m

        