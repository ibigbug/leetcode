# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if not head or not head.next:
            return None

        fast = head
        for i in range(0, n):
            fast = fast.next

        if not fast:
            return head.next

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
