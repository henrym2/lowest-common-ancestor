# Lowest common ancestor - Matthew Henry
from binarytree import bst, Node

def findPath(root: bst, path: list, key: int):
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

def findLCA(root: Node, key_one: int, key_two: int):
    path_one = list()
    path_two = list()

    # if no path is found, return -1
    if(not findPath(root, path_one, key_one) or not findPath(root, path_two, key_two)):
        return -1

    i = 0
    while(i < len(path_one) and i < len(path_two) and (path_one[i] == path_two[i])):
        i += 1
    return path_one[i-1]