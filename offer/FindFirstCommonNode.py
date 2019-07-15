# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return

        countHead1 = 0
        countHead2 = 0

        backupHead1 = pHead1
        backupHead2 = pHead2
        while backupHead1:
            countHead1 += 1
            backupHead1 = backupHead1.next
        while backupHead2:
            countHead2 += 1
            backupHead2 = backupHead2.next
        
        if countHead1 >= countHead2:
            pHeadLong = pHead1
            pHeadShort = pHead2
        else:
            pHeadLong = pHead2
            pHeadShort = pHead1

        distance = abs(countHead1 - countHead2)
        while pHeadLong.next and distance > 0:
            distance -= 1
            pHeadLong = pHeadLong.next
        while pHeadLong and pHeadShort:
            if pHeadLong != pHeadShort:
                pHeadLong = pHeadLong.next
                pHeadShort = pHeadShort.next
            else:
                return pHeadLong
