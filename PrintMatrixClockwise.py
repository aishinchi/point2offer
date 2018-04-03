# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return None
        row = len(matrix)
        col = len(matrix[0])
        start = 0

        savelist = []
        while row > start * 2 and col > start * 2:
            savelist = self.printMatrixClockwise(matrix, savelist, row, col, start)
            start += 1
        return savelist

    def printMatrixClockwise(self, matrix, savelist, row, col, start):
        endX = col - start - 1
        endY = row - start - 1

        # 从左->右
        for i in range(start, endX+1):
            savelist.append(matrix[start][i])

        # 从上->下
        if start < endY:
            for i in range(start + 1, endY+1):
                savelist.append(matrix[i][endX])

        # 从右->左
        if start < endX and start < endY:
            i = endX - 1
            while i >= start:
                savelist.append(matrix[endY][i])
                i -= 1

        if start < endX and start < endY - 1:
            i = endY - 1
            while i >= start + 1:
                savelist.append(matrix[i][start])
                i -= 1

        return savelist

a = Solution()
print(a.printMatrix([[1],[2],[3],[4],[5]]))