# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0.0:
            return 1.0
        if exponent == 0:
            return 1.0
        if exponent == 1:
            return base
        if exponent == -1:
            return 1.0/base
        absOfExponent = abs(exponent) - 2
        product = base * base
        #Python没有无符号整数，所以右移越界后会无限循环，所以先判断是否大于2能够有效保障不会右移越界
        while absOfExponent >= 2 :
            absOfExponent = int(absOfExponent >> 1)
            product = product * product
        if exponent & 0x01 == 1:
            product = product * base
        if exponent > 0:
            return product
        else:
            return 1.0/product
