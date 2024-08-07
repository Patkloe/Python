def printlevelorder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)
        print()
 
 
def printGivenLevel(root, level):
    if root is None:
        return root
 
    if level == 1:
       #a=0
       print(root.data, end=' ')
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)
 
 
""" Compute the height of a tree--the number of nodes
 along the longest path from the root node down to
 the farthest leaf node
"""
 
 
def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
print("Level order traversal of binary tree is -")
printlevelorder(root)
