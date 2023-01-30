# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        length=0
        temp=head
        while temp!=None:
            length+=1
            temp=temp.next
        new_node=head
        for i in range(length//2):
            new_node=new_node.next
        return new_node
