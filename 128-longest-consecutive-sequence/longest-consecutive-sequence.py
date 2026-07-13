class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        max_num=0
        
        for num in nums:
            if num-1 not in nums:
                current_num=num 
                count=1
                while current_num+1 in nums:
                    count+=1 
                    current_num+=1 
                max_num=max(max_num,count)
        return max_num


        