# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == None:
            return []
        list1 = []
        while listNode.next != None:
            list1.append(listNode.val)
            listNode = listNode.next
        list1.append(listNode.val)  #不要忘了最后一个结点
        return list1[::-1]