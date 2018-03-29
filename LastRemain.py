# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0 or m <= 0:
            return -1
        count = n
        i = 0
        listOfNumber = list(range(n))
        while count > 1:
            i = (i + m - 1 ) % count
            listOfNumber.remove(listOfNumber[i])
            count -= 1
        return listOfNumber[0]