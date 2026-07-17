class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr=[]
        xo=0
        for i in range(n):
            res=start+2*i
            xo=xo^res 
        return xo

            