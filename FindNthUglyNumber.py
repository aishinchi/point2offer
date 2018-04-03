# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0

        uglyNumber = [1]
        tempList = [2, 3, 5]
        count = 1
        while count < index:
            tempMin = min(tempList)
            uglyNumber.append(tempMin)
            tempList.remove(tempMin)
            temp1 = uglyNumber[count] * 2
            if temp1 not in tempList:
                tempList.append(temp1)
            temp2 = uglyNumber[count] * 3
            if temp2 not in tempList:
                tempList.append(temp2)
            temp3 = uglyNumber[count] * 5
            if temp3 not in tempList:
                tempList.append(temp3)
            count += 1
        return uglyNumber[index - 1]

a = Solution()
print(a.GetUglyNumber_Solution(8))