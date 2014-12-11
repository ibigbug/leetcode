# Link: https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        d = {}
        start = 0
        maxlen = 0
        for i, c in enumerate(s):
            if c not in d.keys():
                if (i - start + 1) > maxlen:
                    maxlen = i - start + 1
                d[c] = i
            else:
                for _ in range(start, d[c]):
                    d.pop(s[_])
                start = d[c] + 1
                d[c] = i

        return maxlen
