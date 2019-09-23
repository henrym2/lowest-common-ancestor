# Lowest common ancestor - Matthew Henry
from binarytree import tree, bst, Node

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
    while(i < len(path1) and i < len(path2) and (path1[i] == path2[i])):
        i += 1
    return path1[i-1]