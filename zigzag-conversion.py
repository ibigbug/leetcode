# Link: https://leetcode.com/problems/zigzag-conversion/

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        ret = ['' for i in range(0, len(s))]

        i = 0
        gap = nRows - 2

        while i < len(s):
            j = 0
            while i < len(s) and j < nRows:
                ret[j] += s[i]
                i += 1
                j += 1
            j = gap
            while i < len(s) and j > 0:
                ret[j] += s[i]
                i += 1
                j -= 1
        t = ''
        for i in range(0, len(s)):
            t += ret[i]
        return t

