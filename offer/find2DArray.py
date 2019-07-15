class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == [[]]: # it is very important to pass all the test cases
            return False
        numRows = len(array)
        numCols = len(array[0])
        i = numRows - 1
        j = 0
        currentValue = array[i][j]
        while i >= 0 and j < numCols:
            currentValue = array[i][j]
            if target<currentValue:
                i -= 1
            elif target>currentValue:
                j += 1
            else:
                return True
        



if __name__ == "__main__":
    array = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17],[18,21,23,26]]
    target = 9
    solution = Solution()
    indicateFind = solution.Find(target, array)
    print(indicateFind)