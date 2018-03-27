# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        list1 = [0,1,2]
        j = 3
        while j <= number:
            list1.append(list1[j-1] + list1[j-2])
            j = j + 1
        return list1[number]