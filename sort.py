class Sort:
    #*******************************************************************************************
    #                                             交换排序
    #*******************************************************************************************

    #------------------------------------------------------------------------------------------
    # 1. 冒泡排序：
    # 最好情况：已经有序，在外层循环加一个辅助变量found，则只跑一轮循环比较n-1次即可，时间O(n)
    # 最坏情况：共冒泡 n-1 趟，第 i 趟对比 n-i 次，时间复杂度为O(n*n)
    # 平均情况：O(n*n)
    # 空间复杂度：O(1)
    # 稳定性：稳定，因为在冒泡过程中可以设置，相等的元素不交换
    #------------------------------------------------------------------------------------------
    def BubbleSort(self, lists):
        for i in range(len(lists)-1):
            found = False
            for j in range(len(lists)-i-1):
                if lists[j]>lists[j+1]:
                    lists[j], lists[j+1] = lists[j+1], lists[j]
                    found = True
            if not found:
                break
        print(lists)

    #------------------------------------------------------------------------------------------
    # 1. 快速排序：
    # 首先在整个算法中，记录移动的次数不大于比较的次数，因此时间复杂度只考虑比较次数
    # 最好情况：如果每次划分都可把处理区域划分为长度基本相等的两段，显然只需logn次划分，而在每层划分中
    #          比较次数不超过序列长度，所以时间复杂度为O(nlogn)
    # 最坏情况：如果序列已经是升序或者降序，这时每次划分两段中总有一段为空，另一段长度只比划分前少一个
    #          所以需要n-1次划分，显然这时候时间复杂度为O(n*n)
    # 平均情况：O(nlogn)
    # 空间复杂度：O(logn~n) i,j和标记值，这与算法的递归深度有关，因为采用递归必须用栈把变量存起来
    # 稳定性：不稳定，如果序列是 (15, 8, 17, 8, 34)，上来8放到首位，稳定性就破坏了
    #------------------------------------------------------------------------------------------
    def QuickSort(self, lists, left, right):
        if left >= right:
            return
        
        mid = self.Partition(lists, left, right)
        self.QuickSort(lists, left, mid-1)
        self.QuickSort(lists, mid+1, right)  
        return lists # 这里其实不需要返回值，因为是引用传递

    def Partition(self, arr, left, right):
        keyVal = arr[left]                               # 1. 将标记值设为序列最左面一个数，以便空出一个交换位置
        while left < right:
            while left < right and arr[right] >= keyVal: # 2. 从右面开始扫描(因为左面有空位)，只要大于key值就左移
                right -= 1
            if left < right:                             # 3. 之后将右面比key值小的数移到左空位，并让左索引右移一位
                arr[left] = arr[right]
                left += 1
            while left < right and arr[left] <= keyVal:  # 4. 再从左面扫描(此时右面有空位),只要小于key值就右移
                left += 1
            if left < right:                             # 5. 之后将左面比key值大的数移到右空位，并让右索引左移一位
                arr[right] = arr[left]
                right -= 1
        arr[left] = keyVal                               # 6. 最后让左索引位置的值等于key值，完成一轮快排
        return left

    #*******************************************************************************************
    #                                         插入排序
    #*******************************************************************************************

    #------------------------------------------------------------------------------------------
    # 1. 插入排序：
    # 最好情况：有序，O(n)，每次内层比较一次就结束了内层循环，复杂度在于外层循环
    # 最坏情况：逆序 O(n*n)
    # 平均情况：O(n*n)
    # 空间复杂度：O(1)
    # 稳定性：稳定，因为在内存循环中检索插入位置的过程中，一旦发现当前元素与前面元素相等就不移动了
    #------------------------------------------------------------------------------------------
    def InsertSort(self, lists):
        for i in range(1, len(lists)):        # 开始时第一位的元素默认有序
            x = lists[i]                      # 1. 取无序序列的第一个值为标记值
            j = i                             # 2. 让索引从无序序列第一个值开始
            while j > 0 and lists[j - 1] > x: # 3. 有序序列的最后一个值大于标记值，就后移有序值
                lists[j] = lists[j - 1]       # 4. 找插入位置
                j -= 1
            lists[j] = x                      # 5. 让当前索引值等于标记值，这一步就是插入排序的核心

    #*******************************************************************************************
    #                                         选择排序
    #*******************************************************************************************

    #------------------------------------------------------------------------------------------
    # 1. 选择排序：
    # 最好情况：有序，O(n*n)，外层肯定要走，而且无论如何，内层循环都要走一遍才知道最小值
    # 最坏情况：逆序 O(n*n)
    # 平均情况：O(n*n)，没有适应性，即无论对什么样的序列时间复杂度都一样，性能不会受输入数据影响
    # 空间复杂度：O(1)
    # 稳定性：不稳定，因为是从左到右一次选择，后选择的加在了后面，不影响顺序
    #------------------------------------------------------------------------------------------
    def SelectSort(self, lists):
        for i in range(len(lists)-1):
            k = i
            for j in range(i, len(lists)):
                if lists[j] < lists[k]:
                    k = j
            if i != k:
                lists[i], lists[k] = lists[k], lists[i]

    #------------------------------------------------------------------------------------------
    # 1. 堆排序：
    # 堆是一种特殊的树，要求一个堆是一个完全二叉树，即除了最后一层，其它层的节点个数都是满的，并且最后
    # 一层的节点靠左排列。另外对重每个节点的值都必须大于等于或者小于等于子树的每个节点->大顶堆，小顶堆
    # 最好情况：O(n*logn)
    # 最坏情况：O(n*logn)
    # 平均情况：O(n*logn)
    # 空间复杂度：O(1)
    # 稳定性：不稳定
    #------------------------------------------------------------------------------------------
    def HeapSort(self, heap):
        self.BuildMaxHeap(heap)
        # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
        for i in range(len(heap)-1, -1, -1):
            heap[0], heap[i] = heap[i], heap[0]
            self.MaxHeapify(heap, i, 0)

    def BuildMaxHeap(self, heap):  # 构造一个堆，将堆中所有数据重新排序
        heapSize = len(heap)
        for i in range((heapSize -2)//2,-1,-1):  # 自底向上建堆，从最后一个父节点开始调整堆直到第一个根节点0
            self.MaxHeapify(heap, heapSize, i)

    def MaxHeapify(self, heap, heapSize, root):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
        '''
        给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
        父节点：(root-1)//2
        左子节点：2*root + 1
        右子节点：2*root + 2  即：左子节点 + 1
        '''
        left = 2*root + 1
        right = left + 1
        larger = root
        if left < heapSize and heap[larger] < heap[left]:
            larger = left
        if right < heapSize and heap[larger] < heap[right]:
            larger = right
        if larger != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
            heap[larger], heap[root] = heap[root], heap[larger]
            # 递归的对子树做调整
            self.MaxHeapify(heap, heapSize, larger)    

    #*******************************************************************************************
    #                                         其他排序
    #*******************************************************************************************

    #------------------------------------------------------------------------------------------
    # 1. 归并排序：
    # 最好情况：O(n*logn)
    # 最坏情况：O(n*logn)
    # 平均情况：O(n*logn)，没有适应性，即无论对什么样的序列时间复杂度都一样，性能不会受输入数据影响
    # 空间复杂度：O(n),额外的辅助表
    # 稳定性：稳定
    #------------------------------------------------------------------------------------------
    def MergeSort(self, lists):
        shortLen, longLen = 1, len(lists)
        tempList = [None] * longLen
        while shortLen < longLen:
            self.MergePass(lists, tempList, shortLen, longLen)
            shortLen *= 2
            self.MergePass(tempList, lists, shortLen, longLen)
            shortLen *= 2

    def MergePass(self, listFrom, listTo, shortLen, longLen):
        i = 0
        while i + 2 * shortLen < longLen: # 归并长shortLen的两段
            self.Merge(listFrom, listTo, i, i+shortLen, i+2*shortLen)
            i += 2 * shortLen
        if i + shortLen < longLen:
            self.Merge(listFrom, listTo, i, i+shortLen, longLen)
        else:
            for j in range(i, longLen):
                listTo[j] = listFrom[j]
        
    def Merge(self, listFrom, listTo, low, mid, high):
        i, j, k = low, mid, low
        while i < mid and j < high:
            if listFrom[i] <= listFrom[j]:
                listTo[k] = listFrom[i]
                i += 1
            else:
                listTo[k] = listFrom[j]
                j += 1
            k += 1
        while i < mid:
            listTo[k] = listFrom[i]
            i += 1
            k += 1
        while j < high:
            listTo[k] = listFrom[j]
            j += 1
            k += 1 

    #------------------------------------------------------------------------------------------
    # 1. 计数排序：
    # 最好情况：O(n+k)
    # 最坏情况：O(n+k)
    # 平均情况：O(n+k)
    # 空间复杂度：O(k),额外的辅助表
    # 稳定性：稳定
    #------------------------------------------------------------------------------------------
    def CountSort(self, lists):
        n=len(lists)
        num=max(lists)
        count=[0]*(num+1)
        for i in range(0,n):
            count[lists[i]]+=1
        arr=[]
        for i in range(0,num+1):
            for j in range(0,count[i]):
                arr.append(i)
        return arr



if __name__ == "__main__":
    lists = [46, 79, 56, 38, 40, 84]
    sort = Sort()
    # sort.BubbleSort(lists)
    # sortList = sort.QuickSort(lists, 0, len(lists)-1)
    # sortList = sort.HeapSort(lists)
    sortList= sort.MergeSort(lists)
    print(sortList)
