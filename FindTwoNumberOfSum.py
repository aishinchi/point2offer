# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        if tsum < array[0]:
            return []
        array = list(array)
        lens = len(array)
        head = 0
        tail = lens - 1
        for i in range(lens):
            if tail > head:
                if array[tail] + array[head] > tsum:
                    tail -= 1
                elif array[tail] + array[head] < tsum:
                    head += 1
                else:
                    return [array[head],array[tail]]
            elif tail == head:
                return []