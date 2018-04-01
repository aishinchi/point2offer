# -*- coding:utf-8 -*-
#为什么python2用字典实现不行，而python3可以呢？
# class Solution:
#     def FirstNotRepeatingChar(self, s):
#         # write code here
#         dic = dict()
#         lens = len(s)
#         for i in range(lens):
#             if s[i] in dic:
#                 dic[s[i]] += 1
#             else:
#                 dic[s[i]] = 1
#         for item in dic:
#             if dic[item] == 1:
#                 return s.index(item)
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dic = dict()
        lens = len(s)
        for i in range(lens):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        temp = []
        for item in dic:
            if dic[item] == 1:
                temp.append(s.index(item))
        temp.sort()
        return temp[0]
a = Solution()
print(a.FirstNotRepeatingChar('googgle'))
# print(a.FirstNotRepeatingChar('google'))