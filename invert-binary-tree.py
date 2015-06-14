# Link: https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return

        self.swap(root)

        if root.left:
            self.invertTree(root.left)

        if root.right:
            self.invertTree(root.right)

        return root

    def swap(self, node):
        t = node.left
        node.left = node.right
        node.right = t

