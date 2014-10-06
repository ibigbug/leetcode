# Link: https://oj.leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#         self.val = x
#         self.next = None

#     def __str__(self):
#         ret = [str(self.val)]
#         cur = self.next
#         while cur:
#             ret.append(str(cur.val))
#             cur = cur.next
#         return ','.join(ret)

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        val = l1.val + l2.val
        CF = 0
        if val >= 10:
            val %= 10
            CF = 1
        ret = ListNode(val)
        cur = ret


        l, s = self.select_longer(l1, l2)
        l = l.next
        s = s.next
        while l:
            if s is None:
                sval = 0
            else:
                sval = s.val
            val = l.val + sval
            if CF:
                val += 1

            if val >= 10:
                CF = 1
                val %= 10
            else:
                CF = 0
            cur.next = ListNode(val)
            cur = cur.next

            l = l.next
            if s:
                s = s.next

        if CF:
            if cur.next:
                cur.next.val += 1
            else:
                cur.next = ListNode(1)
        return ret


    def select_longer(self, l1, l2):
        cur1 = l1
        cur2 = l2
        while cur1:
            cur1 = cur1.next
            cur2 = cur2.next
            if cur1 is None:
                return (l2, l1)
            if cur2 is None:
                return (l1, l2)

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(9)
    l2.next = ListNode(9)

    s = Solution()
    print(s.addTwoNumbers(l1, l2))
