# Link: https://leetcode.com/problems/container-with-most-water/
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        V = -1
        l = 0
        r = len(height) - 1

        while (l < r):
            s = min(height[l], height[r]) * (r - l)
            V = max(s, V)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return V
