# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and not pHead2:
            return []
        while pHead1 != None and pHead2 != None:
            temp1 = pHead1.next
            temp2 = pHead2.next
            if pHead1.val < pHead2.val:
                if temp1.val < temp2.val:
                    pHead1.next = pHead2
                    pHead2.next = temp1
                elif temp1.val >= temp2.val:
                    pHead1.next = pHead2
            else:
                if temp1.val < temp2.val:
                    pHead2.next = pHead1
                elif temp1.val >= temp2.val:
                    pHead2.next = pHead1
                    pHead1.next = pHead2
            pHead1 = temp1.next
            pHead2 = temp2.next
        return pHead1

a = Solution()
print(a.Merge({1,2,3},{4,5,6}))
