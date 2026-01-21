# Node class for binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Traversal functions

# In-order: Left → Root → Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Pre-order: Root → Left → Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Post-order: Left → Right → Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Function to calculate height of tree
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

# Create the binary tree
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

# Perform traversals
print("In-order traversal:")
inorder(root)   # Output: 3 5 7 10 12 15 18

print("\nPre-order traversal:")
preorder(root)  # Output: 10 5 3 7 15 12 18

print("\nPost-order traversal:")
postorder(root) # Output: 3 7 5 12 18 15 10

# Calculate height
print("\nHeight of tree:", height(root))  # Output: 3
