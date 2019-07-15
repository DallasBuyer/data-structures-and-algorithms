# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        c = Counter(data)
        return c[k]
        
if __name__ == "__main__":
    lists = [1, 2, 2, 4, 4, 4, 5]
    solution = Solution()
    num = solution.GetNumberOfK(lists, 11)
    print(num)