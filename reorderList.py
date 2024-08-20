Link to the problem: https://leetcode.com/problems/reorder-list/editorial/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        #find mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #reverse second half of linked list
        prev = None
        second = slow.next
        slow.next = None
        """ 
                3 -> 4 -> 5 -> NULL
              /      
        prev   sec  nxt
        """
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        # Merge 2 lists
        """
           head                   prev
            1 -> 2 -> 3 -> NULL    5 -> 4 -> NULL
           first tmp1           second tmp2
        """  
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
