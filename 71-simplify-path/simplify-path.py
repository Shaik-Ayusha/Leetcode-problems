class Solution:
    def simplifyPath(self, path: str) -> str:
        part=path.split("/")
        stack=[]
        for ch in part:
            if ch=="" or ch==".":
                continue 
            elif ch=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return "/"+"/".join(stack)