# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        curr = head
        dummy = ListNode()
        l = dummy
        dummy2 = ListNode()
        l2 = dummy2
        while curr:
            if curr.val < x:
                l.next = ListNode(curr.val)
                l = l.next
            else:
                l2.next = ListNode(curr.val)
                l2 = l2.next
            
            curr = curr.next
        l.next = dummy2.next
        print(l2)
        return dummy.next