class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i=0
        n=len(s)
        summed=0
        for j in range(1,n):
            if  roman[s[i]]>=roman[s[j]]:
                summed+=roman[s[i]]
            else:
                summed-=roman[s[i]]
            i+=1
        summed+=roman[s[-1]]
        return summed

