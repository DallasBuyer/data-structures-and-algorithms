# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3] 层次遍历二叉树
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        listVal = []
        dequeNode = []
        dequeNode.append(root)
        while dequeNode:
            currentNode = dequeNode.pop(0)
            listVal.append(currentNode.val)
            if currentNode.left:
                dequeNode.append(currentNode.left)
            if currentNode.right:
                dequeNode.append(currentNode.right)
        
        return listVal
