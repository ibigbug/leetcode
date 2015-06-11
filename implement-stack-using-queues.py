# Link: https://leetcode.com/problems/implement-stack-using-queues/
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = []
        self.cur = -1


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q.append(x)
        self.cur += 1


    # @return nothing
    def pop(self):
        self.q.pop()
        self.cur -= 1

    # @return an integer
    def top(self):
        return self.q[self.cur]

    # @return an boolean
    def empty(self):
        return self.cur == -1

