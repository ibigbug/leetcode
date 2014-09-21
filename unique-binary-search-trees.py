# Link: https://oj.leetcode.com/problems/unique-binary-search-trees/
class Solution:
    # @return an integer
    def numTrees(self, n):
        """
        count(n) = count(0) * count(n-1) +  # means 1 is the root and 0 eles on
        left, n-1 eles on right
                    count(1) * count(n - 2)+
                    ...
                    count(n-1) * count(0)
        """
        if n == 0: return 1
        if n == 1: return 1
        ret = [1, 1]
        ret.extend([ 0 for i in range(2, n + 1)])
        for i in range(2, n + 1):
            for j in range(0, j):
                ret[i] += ret[j] * ret[i - j - 1]
        return ret[n]
