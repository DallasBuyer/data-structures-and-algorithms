# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # Boundary conditions
        if not pRoot1 or not pRoot2:
            return
        
        indicate = False
        if pRoot1.val == pRoot2.val:
            indicate = self.DoesHaveTree2(pRoot1, pRoot2)
        if not indicate:
            indicate = self.HasSubtree(pRoot1.left, pRoot2)
        if not indicate:
            indicate = self.HasSubtree(pRoot1.right, pRoot2)

        return indicate

    def DoesHaveTree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if not pRoot1.val == pRoot2.val:
            return False
        return self.DoesHaveTree2(pRoot1.left, pRoot2.left) and self.DoesHaveTree2(pRoot1.right, pRoot2.right)
        
        
