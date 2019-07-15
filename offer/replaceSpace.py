class Solution:
    def replaceSpace(self, s):
        if not isinstance(s, str) or len(s)<0 or s==None:
            return ''
        spaceNum = 0
        for i in s:
            if i==" ":
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfNew >= 0 and indexOfOriginal <= indexOfNew:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew - 2: indexOfNew + 1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return ''.join(newStr)
    def replaceSpace1(self, s):
        if not isinstance(s, str) or len(s)<0 or s==None:
            return ''
        spaceNum = 0
        for i in s:
            if i==" ":
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = 0, 0
        while indexOfOriginal <= len(s)-1:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew: indexOfNew + 3] = ['%', '2', '0']
                indexOfNew += 3
                indexOfOriginal += 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew += 1
                indexOfOriginal += 1
        return ''.join(newStr)

def main():
    s = 'We are happy'
    solution = Solution()
    newStr  = solution.replaceSpace(s)
    print(newStr)
    newStr1 = solution.replaceSpace1(s)
    print(newStr1)
    

if __name__ == "__main__":
    main()
    # a = 'we are'
    # print(len(a))


        