class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n=str(n)
        non_zeroes=""
        for digits in n:
            if digits!='0':
                non_zeroes+=digits 
        if non_zeroes=='':
            return 0 
        x=non_zeroes 
        res=list(map(int,x))
        summed=sum(res)
        return summed*int(x)