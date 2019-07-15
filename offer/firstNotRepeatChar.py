from collections import Counter
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        listStr = list(s)
        c = Counter(listStr)
        for i in range(len(listStr)):
            if c[listStr[i]] == 1:
                return i
        return -1

if __name__ == "__main__":
    listStr = 'abaccdeff'
    solution = Solution()
    index = solution.FirstNotRepeatingChar(listStr)
    print(index)