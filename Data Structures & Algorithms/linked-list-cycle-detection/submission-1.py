# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPtr, fastPtr = head, head
        while slowPtr and fastPtr:
            slowPtr = slowPtr.next

            if not fastPtr.next:
                return False
                
            fastPtr = fastPtr.next.next

            if slowPtr and fastPtr and slowPtr == fastPtr:
                return True
        return False
            