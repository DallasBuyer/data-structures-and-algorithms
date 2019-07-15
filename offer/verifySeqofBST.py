# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return
        if len(sequence) == 1:
            return True
        root = sequence[-1]
        indexLeft = 0
        while sequence[indexLeft] < root:
            indexLeft += 1

        for j in range(indexLeft, len(sequence)-1, 1):
            if sequence[j] < root:
                return False
        
        left = True
        right = True
        if indexLeft > 0:
            left = self.VerifySquenceOfBST(sequence[:indexLeft])
        if indexLeft < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[indexLeft:-1])
        
        return left and right

if __name__ == "__main__":
    lists = [4, 6, 7, 5]
    solution = Solution()
    res = solution.VerifySquenceOfBST(lists)
    print(res)