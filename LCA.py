# Lowest common ancestor - Matthew Henry
# Code modified from Geeks2Geeks tutorial on LCA in b-tree
# binary tree module from python used for quick development
from binarytree import bst, Node

def find_path(root, path, key):
    if root is None:
        return False
    
    path.append(root.value)

    if root.value == key:
        return True

    if (root.left != None and find_path(root.left, path, key)) or (
        root.right != None and find_path(root.right, path, key)
        ):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False

    path.pop()
    return False

def find_lca(root, key_one, key_two):
    path_one = list()
    path_two = list()

    # if no path is found between the two nodes return -1
    if(not find_path(root, path_one, key_one) or not find_path(root, path_two, key_two)):
        return -1

    i = 0
    while(i < len(path_one) and i < len(path_two) and (path_one[i] == path_two[i])):
        i += 1
    return path_one[i-1]

#DAG Node Class

class DAGnode:
    def __init__(self,key):
        self.key = key
        self.pred = []
        self.succ = []

#BFS between two nodes method
def find_lca_dag(root: DAGnode,  node_1: DAGnode, node_2: DAGnode):
    if type(root) != DAGnode or type(node_1) != DAGnode or type(node_2) != DAGnode:
        return None
    if root is None:
        return None
    if root == node_1 or root == node_2:
        return root
    if node_1 == node_2:
        return node_1.key
    lca = list()
    for i in range(len(node_1.pred)):
        for j in range(len(node_2.pred)):
            if(node_1.pred[i].key == node_2.pred[j].key):
                lca.append(node_1.pred[i].key)
    
    if lca == []:
        if node_1.key > node_2.key:
            lca.append(find_lca_dag(root, node_1.pred[0], node_2))
        else:
            lca.append(find_lca_dag(root, node_1, node_2.pred[0]))

    return max(lca)
