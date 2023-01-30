# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        cur = root = head
        while head:
            if head.val != cur.val:
                cur.next = cur = head
            head = cur.next = head.next
        return root
