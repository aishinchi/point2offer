# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None:
            return None
        count = 1
        while pHead.next != None:
            count += 1
        if count == 1:
            return pHead
        preNode = ListNode(None)
        rearNode = ListNode(pHead.next.val)
        for i in range(count):
            rearNode = pHead.next
            pHead.next = preNode
            preNode = pHead
        return pHead

a = Solution()
a.ReverseList({1,2,3,4,5})