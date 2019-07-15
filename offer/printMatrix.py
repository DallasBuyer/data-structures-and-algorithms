# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        colsLeft = len(matrix[0]) # 剩余未扫描列数
        rowsLeft = len(matrix) # 剩余未扫描行数
        indexRow, indexCol = 0, -1
        rowPlus, colPlus = True, True
        res = []

        while colsLeft > 0 and rowsLeft > 0:
            for ii in range(colsLeft):
                if colPlus:
                    indexCol += 1
                    res.append(matrix[indexRow][indexCol])
                else:
                    indexCol -= 1
                    res.append(matrix[indexRow][indexCol])
            rowsLeft -= 1
            colPlus = not colPlus

            for jj in range(rowsLeft):
                if rowPlus:
                    indexRow = indexRow + 1
                    res.append(matrix[indexRow][indexCol])
                else:
                    indexRow = indexRow - 1
                    res.append(matrix[indexRow][indexCol])
            colsLeft -= 1
            rowPlus = not rowPlus

        return res

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],\
        [5, 6, 7, 8],\
            [9, 10, 11, 12],\
                [13, 14, 15, 16]]  
    solution = Solution()
    solution.printMatrix(matrix)