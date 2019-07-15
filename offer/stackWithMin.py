# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.stackMin = []
        self.minCurrent = 0
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.stackMin:
            if node <= self.minCurrent:
                self.stackMin.append(node)
                self.minCurrent = node
            else:
                self.stackMin.append(self.minCurrent)
        else:
            self.stackMin.append(node)
            self.minCurrent = node
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.stackMin.pop()
        else:
            return
    def top(self):
        # write code here
        if self.stack:
            return self.stack[0]
        else:
            return
    def min(self):
        # write code here
        if self.stackMin:
            print(self.stackMin[-1])
        else:
            return


if __name__ == "__main__":
    solution = Solution()
    solution.push(3)
    solution.min()
    solution.push(4)
    solution.min()
    solution.push(2)
    solution.min()
    solution.push(3)
    solution.min()
    solution.pop()
    solution.min()
    solution.pop()
    solution.min()
    solution.pop()
    solution.min()
    solution.push(0)
    solution.min()
    
