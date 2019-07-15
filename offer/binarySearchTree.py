
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.testValue = 4

    def search(self, root, value):
        node = root
        if node is None:
            return False
        if node.value == value:
            return True
        if node.value > value:
            self.search(node.right, value)
        else:
             self.search(node.left, value)

    def insert(self, root, value):
        if root == None:
            root = Node(value)
        elif value < root.value:
            if root.left == None:
                root.left = Node(value)
            else:
                self.insert(root.left, value)
        elif value > root.value:
            if root.right == None:
                root.right = Node(value)
            else:
                self.insert(root.right, value)
        return root
            
            
    def midTravel(self, root):
        if root == None:
            return
        self.midTravel(root.left)
        print(root.value)
        self.midTravel(root.right)
    
    def change(self, value):
        value = value + 1

if __name__ == "__main__":
    binaryST = BST()
    binaryST.change(binaryST.testValue)
    lists = [3,6,1,12,34,9]
    for i in range(len(lists)):
        binaryST.root = binaryST.insert(binaryST.root, lists[i])
    binaryST.midTravel(binaryST.root)




