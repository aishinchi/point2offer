# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        lens = len(array)
        maxSum = array[0]
        for i in range(lens):
            if i == 0:
                tempSum = array[0]
            else:
                if tempSum <= 0:
                    tempSum = array[i]
                else:
                    tempSum += array[i]
            if tempSum > maxSum:
                maxSum = tempSum
        return maxSum