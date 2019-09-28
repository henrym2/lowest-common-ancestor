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
    path_one = list()
    path_two = list()

    # if no path is found, return -1
    if(not findPath(root, path_one, key_one) or not findPath(root, path_two, key_two)):
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

def findLCADAG(root, node_1, node_2):
    if root is None:
        return None
    if root.key == node_1 or root.key == node_2:
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
            lca.append(findLCADAG(root, node_1.pred[0], node_2))
        else:
            lca.append(findLCADAG(root, node_1, node_2.pred[0]))

    return max(lca)


root = DAGnode(1)
r2 = DAGnode(2)
r3 = DAGnode(3)
r4 = DAGnode(4)
r5 = DAGnode(5)
r6 = DAGnode(6)
root.succ = [r2,r3,r4,r5]
r2.succ = [r4]
r2.pred = [root]
r3.succ = [r4, r5]
r3.pred = [root]
r4.succ = [r5]
r4.pred = [r2,r3,root]
r5.pred = [r3,r4,root]
r6.pred = [r4]

print(findLCADAG(root, root.key, r3.key).key)