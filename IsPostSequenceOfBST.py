# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        lens = len(sequence)
        if not sequence or lens <= 0: #左右子树都不能为空吗？实在不明白
            return False

        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1
        for j in range(i, lens - 1):
            if sequence[j] < root:
                return False
        leftFlag = True
        if i > 0:
            leftFlag = self.VerifySquenceOfBST(sequence[:i])
        rightFlag = True
        if i < lens - 1:
            rightFlag = self.VerifySquenceOfBST(sequence[i:lens - 1])

        return leftFlag and rightFlag


a = Solution()
print(a.VerifySquenceOfBST([5,7,6,9,11,10,8]))