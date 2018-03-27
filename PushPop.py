# -*- coding:utf-8 -*-
class Solution:
    list1 = []
    list2 = []
    def push(self, node):
        # write code here
        self.list1.append(node)
    def pop(self):
        # return xx
        #如果栈2不空，则直接输出栈顶元素并删除；如果栈2为空，则讲栈1赋值给栈2并清空栈1——list存储是下标越大，数据越新
        if not self.list2:
            self.list2 = self.list1
            self.list1 = []
        return self.list2.pop(0)