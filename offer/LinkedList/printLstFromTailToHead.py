# -*- coding:utf-8 -*-

# 题目: 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList

# 解法: 其实这道题本质上是反转链表，不过没有限制说不能开辟新的内存空间，可以用头插法


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        arrayList = []
        while listNode:
            arrayList.insert(0, listNode.val)
            listNode = listNode.next
        return arrayList

if __name__ == "__main__":
    arrayList = [4, 6, 2, 12, 9]
    listHeadNode = ListNode(arrayList[0])
    currentNode = listHeadNode
    for i in range(1, len(arrayList)):
        newNode = ListNode(arrayList[i])
        currentNode.next = newNode
        currentNode = newNode
    
    solution = Solution()
    res = solution.printListFromTailToHead(listHeadNode)
    print(res)