# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 1:
            return []
        small = 1
        big = 2
        bigList = []
        subList = []
        tempSum = big + small
        if tsum == 3:
            return [[1,2]]
        while big > small and big < tsum:
            if tempSum < tsum:
                big += 1
                tempSum += big
            elif tempSum > tsum:
                tempSum -= small
                small += 1
            else:
                subList = list(range(small,big+1))
                bigList.append(subList)
                big += 1
                tempSum += big
        return bigList

a = Solution()
print(a.FindContinuousSequence(9))