# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # return the root node of the reconstructed TreeNode
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre and not tin: # the ending condition for recursion
            return None
        rootNode = TreeNode(pre[0])
        if set(pre) != set(tin):
            return None
        index = tin.index(rootNode.val)
        preNewLeft = pre[1:index+1]
        tinNewLeft = tin[:index]
        rootNode.left = self.reConstructBinaryTree(preNewLeft, tinNewLeft)
        preNewRight = pre[index+1:]
        tinNewRight = tin[index+1:]
        rootNode.right = self.reConstructBinaryTree(preNewRight, tinNewRight)
        return rootNode

def preTravel(rootNode):
    if rootNode==None:
        return
    print(rootNode.val)
    preTravel(rootNode.left)
    preTravel(rootNode.right)

def midTravel(rootNode):
    if rootNode==None:
        return
    midTravel(rootNode.left)
    print(rootNode.val)
    midTravel(rootNode.right)

def afterTravel(rootNode):
    if rootNode==None:
        return
    afterTravel(rootNode.left)
    afterTravel(rootNode.right)
    print(rootNode.val)

def main():
    pre = [1,2,3,4,5,6,7]
    tin = [3,2,4,1,6,5,7]
    solution = Solution()
    rootNode = solution.reConstructBinaryTree(pre, tin)
    return rootNode

if __name__ == "__main__":
    rootNode = main()
    preTravel(rootNode)
    print('\n')
    midTravel(rootNode)
    print('\n')
    afterTravel(rootNode)
