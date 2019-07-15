# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) == 0:
            return []
        left, right = 0, len(array)-1
        num1, num2 = 0, 0
        while left < right:
            sumNum = array[left] + array[right]
            if sumNum == tsum:
                num1 = array[left]
                num2 = array[right]
                break
            elif sumNum < tsum:
                left += 1
            else:
                right -= 1
        if left == right:
            return []
        return num1, num2

if __name__ == "__main__":
    # lists = [1,2,4,7,11,16]
    lists = []
    solution = Solution()
    output = solution.FindNumbersWithSum(lists, 10)
    print(output)
