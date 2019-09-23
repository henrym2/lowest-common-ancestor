# Lowest common ancestor - Matthew Henry
from binarytree import tree, bst, Node

# Generate a random binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root)


def findPath(root, path, k):
    if root is None:
        return False
    
    path.append(root.value)

    if root.value == k:
        return True

    if (root.left != None and findPath(root.left, path, k)) or (
        root.right != None and findPath(root.right, path, k)
        ):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False

    path.pop()
    return False

def findLCA(root, n1, n2):
    path1 = []
    path2 = []

    if(not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root)


print("LCA(4, 5) = %d" %(findLCA(root, 4, 5,))) 
print("LCA(4, 6) = %d" %(findLCA(root, 4, 6)))
print("LCA(3, 4) = %d" %(findLCA(root,3,4))) 
print("LCA(2, 4) = %d" %(findLCA(root,2, 4)))