# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        flag = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                flag = self.HasRoot(pRoot1, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.left, pRoot2)
            if not flag:
                flag = self.HasSubtree(pRoot1.right, pRoot2)
        return flag

    def HasRoot(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.HasRoot(pRoot1.left, pRoot2.left) and self.HasRoot(pRoot1.right, pRoot2.right)