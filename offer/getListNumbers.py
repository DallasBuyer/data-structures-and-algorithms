class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        length = len(tinput)
        if tinput is None or k>length or k<=0:
            return
        left = 0
        right = len(tinput)-1
        output = []
        mid = self.Partition(tinput, left, right)
        while mid != k-1:
            if mid > k-1:
                right = mid - 1
                mid = self.Partition(tinput, left, right)
            else:
                left = mid + 1
                mid = self.Partition(tinput, left, right)
                
        for i in range(k):
            output.append(tinput[i])

        output.sort()
        return output
        
    def Partition(self, lists, left, right):
        key = left
        while left < right:
            while lists[right] >= lists[key] and left < right:
                right -= 1
            while lists[left] <= lists[key] and left < right:
                left += 1
            lists[left], lists[right] = lists[right], lists[left]
            
        lists[key], lists[left] = lists[left], lists[key]
        return left

if __name__ == "__main__":
    lists = [4,5,1,6,2,7,3,8]
    solution = Solution()
    sortList = solution.GetLeastNumbers_Solution(lists, 10)
    print(sortList)