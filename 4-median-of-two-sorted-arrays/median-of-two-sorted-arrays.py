class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)

        n2=len(nums2)

        arr=[0]*(n1+n2)
        i=0 
        j=0 
        k=0 
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                arr[k]=nums1[i]
                i+=1 
                k+=1 
            else:
                arr[k]=nums2[j]
                j+=1 
                k+=1 
        while i<n1:
            arr[k]=nums1[i]
            i+=1 
            k+=1 
        while j<n2:
            arr[k]=nums2[j]
            j+=1 
            k+=1 
        s=len(arr)
        if len(arr)%2==0:
            res=arr[s//2]+arr[(s//2)-1]
            return res/2
        else:
            return arr[s//2]
        