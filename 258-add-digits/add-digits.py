class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            n=num
            digit=0
            while n>0:
                digit+=n%10
                n=n//10
            num=digit
        return num
        