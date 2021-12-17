# Author: OMKAR PATHAK
# https://github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Trees/Tree.py
import sys
class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

    # for setting left node
    def setLeft(self, node):
        self.left = node

    # for setting right node
    def setRight(self, node):
        self.right = node

    # for getting the left node
    def getLeft(self):
        return self.left

    # for getting right node
    def getRight(self):
        return self.right

    # for setting data of a node
    def setData(self, data):
        self.data = data

    # for getting data of a node
    def getData(self):
        return self.data

    def insert(self, data): #def insert(self, val):
        if not self.data:
            self.data = data
            return

        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left = Node(data) # self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(data)
            return
        self.right = Node(data) #self.right = BSTNode(val)


# in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
def inorder(Tree):
    if Tree:
        inorder(Tree.getLeft())
        print(Tree.getData(), end = ' ')
        inorder(Tree.getRight())
    return

# in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
def preorder(Tree):
    if Tree:
        print(Tree.getData(), end = ' ')
        preorder(Tree.getLeft())
        preorder(Tree.getRight())
    return

# in this we first traverse to the leftmost node and then to the rightmost node and then print the data
def postorder(Tree):
    if Tree:
        postorder(Tree.getLeft())
        postorder(Tree.getRight())
        print(Tree.getData(), end = ' ')
    return

def height_of_BST(bst):
#    '''Returns the height of the BST created'''
    if bst == None: 
      return 0
    else: 
      #return 1 + max(height_of_BST(bst.leftChild), height_of_BST(bst.rightChild))
      return 1 + max(height_of_BST(bst.left), height_of_BST(bst.right))

def solve():
    user1 = sys.stdin.readline().split()
    nums = sys.stdin.readline().split(",")
    # 8
    # 7,4,1,5,12,8,9,15
    #print("\n nums:",nums)
    root = Node()
    for num in nums:
        root.insert(int(num))
    #print('\nPostorder Traversal:')   
    #postorder(root)
    preorder(root)
    print()

if __name__ == '__main__':
    #import sys
    n = int(sys.stdin.readline())
    for i in range(n):
        solve()      


