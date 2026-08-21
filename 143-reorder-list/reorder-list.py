# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head 
        fast=head 
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 

        remaining=slow.next 
        slow.next=None 
        temp=remaining
        stack=[]

        while temp:
            stack.append(temp.val)
            temp=temp.next
        temp = head

        while stack:
            value = stack.pop()

            new_node = ListNode(value)

            next_node = temp.next

            temp.next = new_node
            new_node.next = next_node

            temp = next_node

        

        