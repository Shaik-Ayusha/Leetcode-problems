# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        length=0
        curr=head
        while temp:
            temp=temp.next 
            length+=1
        if length==1:

            return None
        elif length==n:
            return head.next 

        res=length-n 
        for i in range(res-1):
            curr=curr.next
        
        curr.next=curr.next.next
        return head


        