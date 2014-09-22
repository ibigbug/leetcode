# Link: https://oj.leetcode.com/problems/two-sum/

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        """
        use hashtable
        """
        d = {}
        index1 = index2 = 0
        for i in range(0, len(num)):
            if (target - num[i]) in d:
                index1 = d[target - num[i]]
                index2 = i
                break
            else:
                d[num[i]] = i
        return (index1 + 1, index2 + 1)
