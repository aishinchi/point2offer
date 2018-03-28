# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code her
        count = 0
        if n < 0:
            n = n&0xffffffff
        while n :
            n = (n - 1) & n
            count = count + 1
        return count