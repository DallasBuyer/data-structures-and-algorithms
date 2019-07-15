# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if (root is None):
            return []
        if (root and not root.left and not root.right and root.val == expectNumber):
            return [[root.val]]
        pathList = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for i in (left + right):
            pathList.append([root.val] + i)
        return pathList

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(12)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(7)
    expectNumber = 22
    solution = Solution()
    solution.FindPath(root, expectNumber)


        