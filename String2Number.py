# -*- coding:utf-8 -*-
#用字典原子实现str和int的转变，但是边界条件没有考虑清楚（python的int最大是？）
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0
        s = s.lstrip(' ')
        lens = len(s)
        list2 = []
        res = 1
        if s[0] == '+' or s[0] == '-':
            if s[0] == '-':
                res = -1
            for i in range(1,lens):
                if '0' <= s[i] <= '9':
                    list2.append(s[i])
                else:
                    return 0
        elif '0' <= s[0] <= '9':
            for i in range(lens):
                if '0' <= s[i] <= '9':
                    list2.append(s[i])
                else:
                    return 0
        else:
            return 0
        lenOfNum = len(list2)
        num = 0
        dic ={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        for i in range(1,lenOfNum+1):
            num = num + dic[list2[-i]]*10**(i-1)
        return res*num
a = Solution()
print(a.StrToInt('-123'))