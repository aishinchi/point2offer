# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:  # 所以[]、{}等都不等于None，所以不能用！= None 进行判断
            return None
        root = TreeNode(pre.pop(0))  # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root
