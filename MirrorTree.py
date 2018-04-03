# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        if root.left != None:
            self.Mirror(root.left)

        if root.right != None:
            self.Mirror(root.right)

            return root


a = Solution()
print(a.Mirror({1,2,3,4,5}))