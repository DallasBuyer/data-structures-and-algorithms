# -*- coding:utf-8 -*-
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        list1 = [pRoot]
        list2 = []
        result = []
        while list1 or list2:
            tmpRes = []
            while list1:
                popNode = list1.pop(0)
                tmpRes.append(popNode.val)
                if popNode.left:
                    list2.append(popNode.left)
                if popNode.right:
                    list2.append(popNode.right)
            if tmpRes:
                result.append(tmpRes)
            tmpRes = []
            while list2:
                popNode = list2.pop(0)
                tmpRes.append(popNode.val)
                if popNode.left:
                    list1.append(popNode.left)
                if popNode.right:
                    list1.append(popNode.right)
            if tmpRes:
                result.append(tmpRes)
        return result

if __name__ == "__main__":
    lists = range(1, 16)
    node1, node2, node3, node4, node5, node6, node7, node8, \
        node9, node10, node11, node12, node13, node14, node15 \
            = [TreeNode(x) for x in lists]
    node1.left, node1.right = node2, node3 
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node4.left, node4.right = node8, node9
    node5.left, node5.right = node10, node11
    node6.left, node6.right = node12, node13
    node7.left, node7.right = node14, node15

    solution = Solution()
    res = solution.Print(node1)
    print(res)