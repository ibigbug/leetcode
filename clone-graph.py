# Link: https://leetcode.com/problems/clone-graph/
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        q = []
        m = {}
        head = UndirectedGraphNode(node.label)
        q.append(node)
        m[node] = head

        while (len(q)):
            curr = q.pop()

            for neighbor in curr.neighbors:
                if m.get(neighbor):
                    m.get(curr).neighbors.append(m.get(neighbor))
                else:
                    copy = UndirectedGraphNode(neighbor.label)
                    m[neighbor] = copy
                    m.get(curr).neighbors.append(copy)
                    q.append(neighbor)

        return head
