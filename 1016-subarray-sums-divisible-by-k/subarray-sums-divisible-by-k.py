class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prefix=0
        count=0 
        dic={0:1}
        for i in range(n):
            prefix+=nums[i]
            if prefix%k in dic:
                count+=dic[prefix%k]
            dic[prefix%k]=dic.get(prefix%k,0)+1 
        return count
        