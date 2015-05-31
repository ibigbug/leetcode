# Link: https://leetcode.com/problems/longest-common-prefix/
class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not len(strs):
            return ''
        if len(strs) == 1:
            return strs[0]

        ret = []
        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != strs[0][i]:
                    return ''.join(ret)
            ret.append(strs[0][i])
        return ''.join(ret)
