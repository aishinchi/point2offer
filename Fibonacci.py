# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 2
        #使用循环和列表，把斐波那契数列存在一个列表中就可以实现更新
        list1 = [0,1]
        while i <= n:
            list1.append(list1[i-1]+list1[i-2])
            i = i + 1
        return list1[n]