# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    pHead3 = ListNode(0)
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        if pHead1 != None and pHead2 != None:
            if pHead1.val < pHead2.val:
                tempNode = pHead1
                self.pHead3 = pHead1
                pHead1 = tempNode.next
                self.pHead3.next = self.Merge(pHead1, pHead2)
            else:
                tempNode = pHead2
                self.pHead3 = pHead1
                pHead2 = tempNode.next
                self.pHead3.next = self.Merge(pHead1, pHead2)
        return self.pHead3


a = Solution()
print(a.Merge({1, 3, 5}, {2, 4, 6}))