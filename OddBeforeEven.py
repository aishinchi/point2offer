# -*- coding:utf-8 -*-
#这不是很明智的做法，因为多申请了两个列表的空间，时间复杂度为O(n)但是空间复杂度为O(n)
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return []
        list1 = []
        list2 = []
        length = len(array)
        for i in range(length):
            if array[i] % 2 == 1:
                list1.append(array[i])
            else:
                list2.append(array[i])
        return list1+list2

