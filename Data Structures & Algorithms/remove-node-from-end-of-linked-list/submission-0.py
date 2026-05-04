# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        if length <= 1: return None

        prev = None
        curr = head
        target = length - n
        currIndex = 0

        while curr:
            if currIndex == target:
                if prev: prev.next = curr.next
                if head == curr: head = head.next
                curr.next = None

            prev = curr
            curr = curr.next
            currIndex += 1
        return head