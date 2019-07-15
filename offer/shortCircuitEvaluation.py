# -*- coding:utf-8 -*-
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
#而“||”运算符表示“或”，有一个为真则全部为真；前半部分判断出来是真的，后半部分就不再进行运算了。
#同理对于“&&”运算符，前一项为假则整个表达式为假，我们利用这个性质可以进行递归运算或者达到整洁代码的目的

class Solution:
    def Sum_Solution(self, n):
        # write code here
        result = n
        return result and result+self.Sum_Solution(n-1)

if __name__ == "__main__":
    n = 3
    solution = Solution()
    res = solution.Sum_Solution(1)
    print(res)