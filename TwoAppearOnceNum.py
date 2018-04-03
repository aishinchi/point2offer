# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array == None:
            return []
        lens = len(array)
        dic = dict()
        for i in range(lens):
            if array[i] in dic:
                dic[array[i]] += 1
            else:
                dic[array[i]] = 1
        tempList = []
        for item in dic:
            if dic[item] == 1:
                tempList.append(item)
        return tempList

a = Solution()
print(a.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))