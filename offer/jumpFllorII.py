class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        listNumber = [1, 2]
        if number >= 3:
            for i in range(number-2):
                listNumber.append(sum(listNumber))
            return listNumber[-1]

if __name__ == "__main__":
    number = 7
    solution = Solution()
    res = solution.jumpFloorII(number)
    print(res)