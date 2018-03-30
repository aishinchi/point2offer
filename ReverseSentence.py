# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        if s == "":
            return ""
        bigList = []
        subList = ""
        lens = len(s)
        for i in range(lens):
            if s[i] == " ":
                bigList.append(subList)
                subList = ""
            else:
                subList = subList + s[i]
        bigList.append(subList)
        bigList = bigList[::-1]
        out = bigList[0]
        for j in range(1,len(bigList)):
            out += " "
            out += bigList[j]
        return out

a = Solution()
print(a.ReverseSentence("student. a am I"))