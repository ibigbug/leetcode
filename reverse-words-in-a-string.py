# Link: https://oj.leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        """
        maybe a faster algo exists ?
        """
        ret = []
        s = s.split(' ')
        for i in range(0, len(s)):
            w = s[len(s) - i - 1].strip()
            if w == '': continue
            ret.append(w)

        return ' '.join(ret)
