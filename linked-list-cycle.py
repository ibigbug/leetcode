class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head: return False
        slow = fast = head
        while fast:
            for i in range(0, 2):
                if fast.next == slow:
                    return True
                if fast.next is None:
                    return False
                fast = fast.next
            slow = slow.next
        return False
