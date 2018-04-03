# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data :
            return 0
        if k < data[0] or k > data[-1]:
            return 0
        count = 0
        lens = len(data)
        for i in range(lens):
            if data[i] == k:
                count += 1
            elif data[i] > k:
                return count
        return count