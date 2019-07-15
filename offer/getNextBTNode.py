# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right: # 如果有右子节点，则把此节点当做根节点，返回其右子节点
            res = pNode.right
            while res.left: # 返回右子节点也就是返回右子树的最左子节点
                res = res.left
            return res
        while pNode.next: # 如果有根节点，则把此节点当做是叶子节点
            temp = pNode.next
            if temp.left == pNode: # 如果此叶节点是左叶子节点，则返回根节点
                return temp
            pNode = temp # 如果此叶节点是右子节点，则一直回溯到某个左子节点
        return None # 如果右子节点回溯完成没有找到找到一个左子节点就返回空
            