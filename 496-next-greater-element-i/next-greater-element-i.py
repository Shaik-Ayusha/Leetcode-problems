class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n=len(nums2)
        stack=[]
        dic={}
        ans=[]
        for ch in nums2:
            dic[ch]=-1
        for i in range(n):
            while stack and nums2[i]>nums2[stack[-1]]:
                curr_num=stack.pop()
                dic[nums2[curr_num]]=nums2[i]
            stack.append(i)
        for num in nums1:
            ans.append(dic[num])
        return ans
        