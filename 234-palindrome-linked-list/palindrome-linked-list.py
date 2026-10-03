# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next 
            fast=fast.next.next 
        second_half=slow.next 
        temp=second_half 
        prev=None 
        while temp:
            next=temp.next 
            temp.next=prev 
            prev=temp
            temp=next
        left=head 
        right=prev 
        while right:
            if right.val!=left.val:
                return False 
            right=right.next 
            left=left.next 
        return True

        

        