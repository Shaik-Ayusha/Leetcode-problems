class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        for ch in t:
            need[ch]=need.get(ch,0)+1
        have=0 
        dic={}
        min_len=float('inf')
        min_start=0
        r=0
        l=0 
        n=len(s)
        need_count=len(need)
        while r<n:
            ch=s[r]
            dic[ch]=dic.get(ch,0)+1 
            if ch in need and dic[ch]==need[ch]:
                have+=1 
                while have==need_count:
                    if r-l+1<min_len:
                        min_len=r-l+1 
                        min_start=l
                    left=s[l]
                    dic[left]-=1
                    l=l+1 
                    if left in need and dic[left]<need[left]:
                        have-=1
            r=r+1 
        if min_len==float('inf'):
            return ""
        return s[min_start:min_len+min_start]
