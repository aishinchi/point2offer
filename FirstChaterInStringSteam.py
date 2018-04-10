# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.count = []
    def FirstAppearingOnce(self):
        # write code here
        if self.count:
            return self.count[0]
        else:
            return "#"

    def Insert(self, char):
        # write code here
        try:
            check = self.count.index(char)
            self.count.pop(check)
        except ValueError:
            self.count.append(char)

a = Solution()
a.Insert('g')
print(a.FirstAppearingOnce())
a.Insert('o')
print(a.FirstAppearingOnce())
a.Insert('o')
print(a.FirstAppearingOnce())
a.Insert('g')
print(a.FirstAppearingOnce())
a.Insert('l')
print(a.FirstAppearingOnce())
a.Insert('e')
print(a.FirstAppearingOnce())