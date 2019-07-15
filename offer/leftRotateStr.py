# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        s1 = s[:n]
        s2 = s[n:]
        return s2+s1

        

if __name__ == "__main__":
    string = 'abcdefg'
    solution = Solution()
    strRes = solution.LeftRotateString(string, 2)
    print(strRes)