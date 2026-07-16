class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        count=0
        
        while temp>0:
            digits=temp%10 
            if  digits!=0 and num%digits==0:
                count+=1

            temp=temp//10
        return count
        