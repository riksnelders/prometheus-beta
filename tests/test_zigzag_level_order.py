import pytest
from src.zigzag_level_order import TreeNode, zigzag_level_order

def test_empty_tree():
    """Test traversal of an empty tree"""
    assert zigzag_level_order(None) == []

def test_single_node_tree():
    """Test traversal of a tree with a single node"""
    root = TreeNode(1)
    assert zigzag_level_order(root) == [[1]]

def test_simple_tree():
    """Test a simple tree with multiple levels"""
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    expected = [
        [3],        # First level (left to right)
        [20, 9],    # Second level (right to left)
        [15, 7]     # Third level (left to right)
    ]
    
    assert zigzag_level_order(root) == expected

def test_asymmetric_tree():
    """Test a tree with an asymmetric structure"""
    #         1
    #       /   \
    #      2     3
    #     /     / \
    #    4     5   6
    #         \
    #          7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.right = TreeNode(7)
    
    expected = [
        [1],            # First level (left to right)
        [3, 2],         # Second level (right to left)
        [4, 5, 6],      # Third level (left to right)
        [7]             # Fourth level (right to left)
    ]
    
    assert zigzag_level_order(root) == expected

def test_large_tree():
    """Test a larger tree to ensure consistency"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    
    expected = [
        [1],                # First level (left to right)
        [3, 2],             # Second level (right to left)
        [4, 5, 6, 7],       # Third level (left to right)
        [9, 8]              # Fourth level (right to left)
    ]
    
    assert zigzag_level_order(root) == expected