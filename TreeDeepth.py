class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0

        leftTree = self.TreeDepth(pRoot.left)
        rightTree = self.TreeDepth(pRoot.right)

        if leftTree > rightTree:
            return leftTree + 1
        else:
            return rightTree + 1