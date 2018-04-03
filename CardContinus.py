# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        temp = []
        for j in range(5):
            if numbers[j] > 0:
                temp.append(numbers[j])
        lens = len(temp)
        numberOfZero = 5 - lens
        if lens == 1:
            return True
        count = 0
        for i in range(1, lens):
            if temp[i] == temp[i - 1]:
                return False
            else:
                count = count + temp[i] - temp[i - 1] - 1
                if count > numberOfZero:  #不需要做完遍历再判断，满足条件即可跳转
                    return False
        return True
