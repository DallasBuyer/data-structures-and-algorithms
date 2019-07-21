# -*- coding:utf-8 -*-

# 题目: 输入一个列表，输出该链表中倒数第k个节点

# 解法: 这类想要从后向前遍历链表的题目，乍一看用O(n*n)肯定可以解，但是时间复杂度太高，
#      其实这是一个减法游戏。既然这里只知道一个K值，那么先让某个指针走K步，则剩下L-K
#      步，如果这个指针走完L-K步的同时，让第二个指针也从头走L-K步则，最终第二个指针
#      就停在了链表的倒数K个节点上。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return
        p1, p2 = head
        count = 0
        while count < k:
            p1 = p1.next
            count += 1