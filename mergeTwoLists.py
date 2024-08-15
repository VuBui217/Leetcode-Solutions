Link to the problem: https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None)
        curr = dummy_head
        while list1 or list2:
            if not list1:
                curr.next = list2
                return dummy_head.next
            if not list2:
                curr.next = list1
                return dummy_head.next
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return dummy_head.next
