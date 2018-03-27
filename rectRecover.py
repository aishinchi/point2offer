# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        i = 3
        list1 = [0,1,2]
        while i <= number:
            list1.append(list1[i-1]+list1[i-2])
            i = i + 1
        return list1[number]