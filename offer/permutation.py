# -*- coding:utf-8 -*-
class Solution: # 这个思路是真的清晰，虽然是递归，但是完全按照正常思维可以想象
    def Permutation(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)
        
        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i > 0 and charList[i] == charList[i-1]:
                continue
            temp = self.Permutation(ss[:i]+ss[i+1:])
            for j in temp:
                pStr.append(charList[i]+j)
        return pStr


if __name__ == "__main__":
    string = 'abc'
    solution = Solution()
    res = solution.Permutation(string)
    print(res)
