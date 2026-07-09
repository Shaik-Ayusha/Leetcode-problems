class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1 
        dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        arr=[]
        for pairs in range(k):
            arr.append(dic[pairs][0])
        return arr

        