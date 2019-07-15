# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        results = numbers[0]
        times = 1
        for i in range(1,len(numbers)):
            if times == 0:
                results = numbers[i]
                times = 1
            elif numbers[i] == results:
                times += 1
            else:
                times -= 1
        
        Check = self.CheckMoreThanHalf(numbers, results)
        if Check is not True:
            results = 0

        return results

    def CheckMoreThanHalf(self, numbers, res):
        length = len(numbers)
        times = 0
        for i in range(length):
            if numbers[i] == res:
                times += 1

        isMoreThanHalf = True
        if times * 2 <= length:
            isMoreThanHalf = False
        
        return isMoreThanHalf

if __name__ == "__main__":
    lists = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    solution = Solution()
    res = solution.MoreThanHalfNum_Solution(lists)