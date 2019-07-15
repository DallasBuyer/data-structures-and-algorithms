# -*- coding:utf-8 -*-
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        L2R = [pRoot]
        R2L = []
        result = []
        while L2R or R2L:
            tmpRes = []
            while L2R:
                popNode = L2R.pop()
                tmpRes.append(popNode.val)
                if popNode.left:
                    R2L.append(popNode.left)
                if popNode.right:
                    R2L.append(popNode.right)
            if tmpRes:
                result.append(tmpRes)
            tmpRes = []
            while R2L:
                popNode = R2L.pop()
                tmpRes.append(popNode.val)
                if popNode.right:
                    L2R.append(popNode.right)
                if popNode.left:
                    L2R.append(popNode.left)
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

