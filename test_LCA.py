# Lowest common ancestor test - Matthew Henry
import LCA

from binarytree import Node, bst
import pytest


def test_single_node_tree():
    root = Node(1)
    print(root)
    assert LCA.find_lca(root, 1, 1) is 1

def test_3_node_balanced():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(root)
    assert LCA.find_lca(root, 1, 1) is 1

def test_unbalanced_5_node():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print(root)
    assert LCA.find_lca(root, 6,7) is 3

def test_random_height_3():
    root = bst(height=3, is_perfect=True)
    print(root)
    assert LCA.find_lca(root, 2, 6) is 3
    assert LCA.find_lca(root, 4, 6) is 5
    assert LCA.find_lca(root, 0, 14) is 7

def test_random_height_5():
    root = bst(height=5, is_perfect=True)
    print(root)
    assert LCA.find_lca(root, 4, 7) is 7
    assert LCA.find_lca(root, 2, 22) is 15
    assert LCA.find_lca(root, 26, 56) is 31
    assert LCA.find_lca(root, 17, 25) is 23

def test_no_path():
    root = bst(height=3, is_perfect=True)
    assert LCA.find_lca(root, 99, 99) is -1
    assert LCA.find_lca(root, 15, 11) is -1