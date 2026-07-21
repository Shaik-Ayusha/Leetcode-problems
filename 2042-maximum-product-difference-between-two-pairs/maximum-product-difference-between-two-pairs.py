class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        largest=0
        s_largest=largest
        smallest=float('inf')
        s_smallest=smallest
        for num in nums:
            if num>largest:
                s_largest=largest
                largest=num 
            elif num >s_largest:
                s_largest=num 
            if num<smallest:
                s_smallest=smallest 
                smallest=num 
            elif num <s_smallest:
                s_smallest=num 
        
        return (largest*s_largest)-(smallest*s_smallest)