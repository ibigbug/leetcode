# Link: https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        la = len(A)
        lb = len(B)
        amount = la + lb
        if amount & 1:  # it's cool !
            return self.findKth(A, B, (la + lb) / 2 + 1)
        return (self.findKth(A, B, (la + lb) / 2) + self.findKth(A, B, (la + lb) / 2 + 1)) / 2.0

    def findKth(self, A, B, k):
        la = len(A)
        lb = len(B)
        if la > lb:
            return self.findKth(B, A, k)  # Assert len(A) < len(B)

        if la == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(k / 2, la)
        pb = k - pa

        if A[pa - 1] < B[pb - 1]:
            return self.findKth(A[pa:], B, k - pa)  # Eleminate the leading `pa`th
        elif A[pa - 1] > B[pb - 1]:
            return self.findKth(A, B[pb:], k - pb)
        else:
            return A[pa - 1]
