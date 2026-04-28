# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        resPtr = res

        while list1 and list2:
            if list1.val <= list2.val:
                resPtr.next = list1
                list1 = list1.next
            else:
                resPtr.next = list2
                list2 = list2.next
            resPtr = resPtr.next

        while list1:
            resPtr.next = list1
            list1 = list1.next
            resPtr = resPtr.next
        while list2:
            resPtr.next = list2
            list2 = list2.next
            resPtr = resPtr.next
        
        return res.next