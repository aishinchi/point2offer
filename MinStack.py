# -*- coding:utf-8 -*-
class Solution:
    stack = []
    minStack = []
    def push(self, node):
        # write code here
        if not self.minStack:
            self.minStack.append(node)
        else:
            self.minStack.append(min(node, self.minStack[-1]))
        self.stack.append(node)
    def pop(self):
        # write code here
        if not self.stack:
            return None
        self.minStack.pop()
        return self.stack.pop() #所以pop()默认是返回并删除最后一个元素？
    def top(self):
        # write code here
        if not self.stack:
            return None
        return self.stack[-1]
    def min(self):
        # write code here
        if not self.minStack:
            return None
        return self.minStack[-1]