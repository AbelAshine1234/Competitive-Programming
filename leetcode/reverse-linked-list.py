# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        while head!=None:
            temp=head
            head=head.next
            temp.next=prev
            prev=temp
        return prev
