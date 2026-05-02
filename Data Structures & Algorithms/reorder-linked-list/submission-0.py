# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast != None:
            if fast.next != None and fast.next.next == None:
                prevTail = fast.next
                fast.next = None
                tempNode = slow.next
                slow.next = prevTail
                prevTail.next = tempNode
                slow = tempNode
                fast = tempNode
            else:
                fast = fast.next
        