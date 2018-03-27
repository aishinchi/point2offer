# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array == None:
            return False
        #最大的问题是没有numpy模块，不知道如何求解数组的维度，可以转换成list，分别求行数和列数
        row = len(array)
        col = len(array[0])
        i = row - 1
        j = 0
        while i > -1 and j < col:
            if array[i][j] < target:
                j = j + 1
            elif array[i][j] > target:
                i = i - 1
            else:
                return True
        return False