# Link: https://oj.leetcode.com/problems/longest-palindromic-substring/


class Solution:
    """
    Will timeout :(
    """
    def longestPalindrome(self, s):
        length = len(s)
        P = [[False for j in range(len(s) + 1)] for i in range(len(s) + 1)]

        max_length = 0
        start = 0
        end = 0

        for i in range(length):
            for j in range(i):
                P[j][i] = (s[j] == s[i]) and (( i - j < 2) or P[j + 1][i - 1])
                if P[j][i] and (max_length < ( i - j + 1)):
                    max_length = i - j + 1
                    start = j
                    end = i

            P[i][i] = True

        return s[start:end + 1]
