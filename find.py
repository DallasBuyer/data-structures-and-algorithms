class Find:
    def seqSearch(self, lists, key):
        length = len(lists)
        if length == 0:
            return False
        for i in range(length):
            if lists[i] == key:
                return i
        else:
            return False

    def binarySearch(self, lists, key):
        length = len(lists)
        if length == 0:
            return False
        begin = 0
        end = length - 1
        while begin <= end:
            mid = (begin + end) // 2
            if lists[mid] > key:
                end = mid - 1
            elif lists[mid] < key:
                begin = mid + 1
            else:
                return True
        return False
    
    def binaryRecursiveSearch(self, lists, key):
        length = len(lists)
        if length == 0:
            return False
        mid = length // 2
        if lists[mid] > key:
            return self.binaryRecursiveSearch(lists[0:mid], key)
        elif lists[mid] < key:
            return self.binaryRecursiveSearch(lists[mid+1:], key)
        else:
            return True

    def insertSearch(self, lists, key):
        length = len(lists)
        if length == 0:
            return False
        begin = 0
        end = length - 1
        while begin <= end:
            mid = begin + int((end - begin) * (key - lists[begin])/(lists[end] - lists[begin]))
            if lists[mid] > key:
                end = mid - 1
            elif lists[mid] < key:
                begin = mid + 1
            else:
                return True
        return False


if __name__ == "__main__":
    lists = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    orderList = [1, 2, 4, 5, 8, 10, 14, 18, 21, 44, 50]
    find = Find()
    results = find.seqSearch(lists, 123)
    # results = find.binaryRecursiveSearch(lists, 54)
    results = find.insertSearch(orderList, 18)
    print(results)