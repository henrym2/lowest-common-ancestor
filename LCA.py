# Lowest common ancestor - Matthew Henry
from binarytree import bst, Node

def findPath(root, path, key):
    if root is None:
        return False
    
    path.append(root.value)

    if root.value == key:
        return True

    if (root.left != None and findPath(root.left, path, key)) or (
        root.right != None and findPath(root.right, path, key)
        ):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False

    path.pop()
    return False

def findLCA(root, key_one, key_two):
    path_one = []
    path_two = []

    if(not findPath(root, path_one, key_one) or not findPath(root, path_two, key_two)):
        return -1

    i = 0
    while(i < len(path_one) and i < len(path_two) and (path_one[i] == path_two[i])):
        i += 1
    return path_one[i-1]