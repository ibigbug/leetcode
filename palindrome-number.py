# Link: https://leetcode.com/problems/palindrome-number/
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        x = str(x)
        for i in range(0, len(x) / 2):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True
