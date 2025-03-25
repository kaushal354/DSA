#assignment 20 (BST ASSIGNMENT 1)
#1. Define a class Node with instance variables left, item and right. The variables left
# and right are used to refer left and right child node. The item variable is used to hold
# data item.
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

# 2.Define a class BST to implement Binary Search Tree data structure. Make __init__()
# method to create root instance variable to hold the reference of root node.
class BST:
    def __init__(self):
        self.root = None

#3. In class BST, define insert method to store new data item in the binary search tree.
    def insert(self,data):
        self.root = self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left,data)
        elif data > root.item:
            root.right = self.rinsert(root.right,data)
        return root

#4. In class BST, define a search method to find a given item in the binary search tree
# and returns the node reference. It returns None if search failed.
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root,data):
        if root is None or root.item == data:
            return root
        if data<root.item:
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)

#5.In class BST, define a method to implement inorder traversal.
    def inorder(self):
        result = []
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root: #if root is false then it is none
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)



#7.In class BST, define a method to implement preorder traversal.
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)

#8.In class BST, define a method to implement postorder traversal.
    def postorder(self):
            result = []
            self.rpostorder(self.root,result)
            return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)

#9. In class BST. define a method to find Minimum value item node.
    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current=current.left
        return current.item

#10. In class BST. define a method to find Maximum value item node.
    def max_value(self,temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item

#11. In class BST. define a method to delete a node from binary search tree
    def delete(self,data):
        self.root = self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left,data)
        elif data > root.item:
            root.right = self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            self.rdelete(root.right,root.item)
        return root

#12. In class BST, define a method size to return the number or elements present in the
# BST.
    def size(self):
        return len(self.inorder())



# Creating a BST instance
bst = BST()

# Inserting elements
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Test inorder traversal (should be sorted order)
assert bst.inorder() == [20, 30, 40, 50, 60, 70, 80]

# Test preorder traversal (root, left, right)
assert bst.preorder() == [50, 30, 20, 40, 70, 60, 80]

# Test postorder traversal (left, right, root)
assert bst.postorder() == [20, 40, 30, 60, 80, 70, 50]

# Test search function
assert bst.search(40) is not None  # Found
assert bst.search(100) is None  # Not Found

# Test finding the minimum and maximum values
assert bst.min_value(bst.root) == 20
assert bst.max_value(bst.root) == 80

# Test size function
assert bst.size() == 7  # 7 elements inserted

# Test deletion
bst.delete(20)  # Deleting leaf node
assert bst.inorder() == [30, 40, 50, 60, 70, 80]

bst.delete(30)  # Deleting node with one child
assert bst.inorder() == [40, 50, 60, 70, 80]

bst.delete(50)  # Deleting root node
assert bst.inorder() == [40, 60, 70, 80]

# Final size check
assert bst.size() == 4

print("All test cases passed!")

