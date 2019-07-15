# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        result = 0
        for obj in array:
            result ^= obj
        index = self.find1Index(result)
        num1, num2 = 0, 0
        for obj in array:
            if self.isBit1(obj, index):
                num1 ^= obj 
            else:
                num2 ^= obj
        return num1, num2

    
    def find1Index(self, digit):
        index = 0
        while not digit & 1:
            digit >>= 1
            index += 1
        return index
    
    def isBit1(self, digit, n):
        digit >>= n
        return digit & 1