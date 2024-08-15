Link to the problem: https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recursion(self, prev, curr):
        if not curr:
            return prev
        next_node = curr.next
        curr.next = prev
        #new_head = self.recursion(curr, next_node)
        return self.recursion(curr, next_node)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Algorithm 1: Iterate the list
        #Using 2 pointers 
        #Reverse the list by switch the pointer of current element to previous element
        #  1  ->  2-> 3-> None
        #  curr
        # prev = None
        # current = head
        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node
        # return prev

        #Alogrithm 2: Using resursion
        return self.recursion(None, head)
