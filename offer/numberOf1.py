class Solution:
    def numberOf1(self, n):
        count = 0
        while(n):
            right = n & 1
            if(right):
                count += 1
            n = n >> 1
        return count


if __name__ == "__main__":
    a = 13
    lists = [3,5]
    b = lists.pop(0)
    a = len(lists)
    solution = Solution()
    count = solution.numberOf1(a)
    print(count)