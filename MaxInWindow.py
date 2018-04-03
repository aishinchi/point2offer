# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size <= 0:
            return []
        num.sort()
        lens = len(num)
        if size > lens:
            return []
        maxList = []
        for i in range(lens-size+1):
            maxList.append(num[size-1+i])
        return maxList

a = Solution()
print(a.maxInWindows([2,3,4,2,6,2,5,1],3))