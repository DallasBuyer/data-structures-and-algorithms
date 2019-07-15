# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None:
            return
        
        Node = ListNode(None)
        Node.next = pHead
        pHead = Node
        pNode = pHead.next  #扫描索引
        preNode = pHead  # 当前节点的前一个节点
        while pNode and pNode.next:
            if pNode.val == pNode.next.val:
                while pNode.val == pNode.next.val:
                    pNode = pNode.next
                    if not pNode.next:
                        break 
                preNode.next = pNode.next
                pNode = preNode.next
            else:
                pNode = pNode.next
                preNode = preNode.next

        return pHead.next


if __name__ == "__main__":
    # lists =  [1, 2, 3, 3, 3, 4, 4, 5]
    lists =  [1, 1, 1]
    lists.reverse()
    pHead = None
    for i in range(len(lists)):
        q = ListNode(lists[i])
        q.next = pHead
        pHead = q
    
    solution = Solution()
    pHead = solution.deleteDuplication(pHead)
    a = 3
