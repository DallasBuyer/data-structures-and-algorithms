# -*- coding:utf-8 -*-
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

class Solution:
    def Add(self, num1, num2):
        # write code here
        carryNum = (num1 & num2) << 1
        sumNum = num1 ^ num2
        while carryNum != 0:
            num1 = carryNum
            num2 = sumNum
            carryNum = (num1 & num2) << 1
            sumNum = num1 ^ num2

        return sumNum

if __name__ == "__main__":
    solution = Solution()
    res = solution.Add(11, 89)
    print(res)