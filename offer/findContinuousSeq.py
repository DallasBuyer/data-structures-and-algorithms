# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        
        left = 1
        right = 2
        sumNum = left + right
        middle = (tsum + 1)/2
        lists = []

        while left < middle:
            if sumNum == tsum:
                lists.append(list(range(left, right+1)))
                right += 1
                sumNum = sumNum + right
            elif sumNum <= tsum:
                right += 1
                sumNum = sumNum + right
            else:
                sumNum = sumNum - left
                left += 1
        return lists

if __name__ == "__main__":
    tsum = 15
    solution = Solution()
    lists = solution.FindContinuousSequence(15)
    print(lists)