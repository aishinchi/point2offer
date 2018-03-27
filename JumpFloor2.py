# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        k = 3
        list1 = [1,2]
        while k <= number:
            list1.append(self.sumofList(list1)+1)
            k = k + 1
        return list1[number-1]
    def sumofList(self,list1):#调用函数记得返回值啊
        sum = 0
        lens = len(list1)
        for i in range(lens):
            sum = sum + list1[i]
        return sum