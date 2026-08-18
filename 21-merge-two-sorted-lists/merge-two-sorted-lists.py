# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
        s1=ListNode()
        head=s1
        while (temp1!=None) and (temp2!=None):
            if temp1.val <temp2.val:
                s2=ListNode(temp1.val)
                s1.next=s2
                s1=s1.next
                temp1=temp1.next 
            else:
                s2=ListNode(temp2.val)
                s1.next=s2 
                s1=s1.next
                temp2=temp2.next 
        if temp1!=None:
            s1.next=temp1 
        elif temp2!=None:
            s1.next=temp2
        return head.next





        