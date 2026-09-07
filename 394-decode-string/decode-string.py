class Solution:
    def decodeString(self, s: str) -> str:
        num=0 
        stack=[]
        curr=""
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch=='[':
                stack.append((curr,num))
                num=0
                curr=''
            elif ch==']':
                res=stack.pop()
                prev,new=res 
                curr=prev+curr*new
            else:
                curr+=ch 
        return curr
        