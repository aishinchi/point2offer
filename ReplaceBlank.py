# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        #新建一个字符串,逐字转换
        if s == None:
            return ""
        s1 = ""
        lens = len(s)
        for i in range(lens):
            if s[i] == " ":
                s1 = s1 + "%20"
            else:
                s1 = s1 + s[i]
        return s1