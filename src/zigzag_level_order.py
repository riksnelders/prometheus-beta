from typing import Optional, List, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[Any]]:
    """
    Perform a zigzag (level order) traversal of a binary tree.
    
    Args:
        root (Optional[TreeNode]): The root node of the binary tree.
    
    Returns:
        List[List[Any]]: A list of levels, where each level is traversed 
                         in a zigzag manner (alternating left-to-right 
                         and right-to-left).
    
    Time Complexity: O(n), where n is the number of nodes in the tree
    Space Complexity: O(w), where w is the maximum width of the tree
    
    Examples:
        1) None input returns empty list
        2) Single node returns list with that node
        3) Handles trees with multiple levels and zigzag pattern
    """
    # Handle empty tree case
    if not root:
        return []
    
    # Use a queue for level-order traversal
    queue = [root]
    result = []
    left_to_right = True
    
    while queue:
        # Get the current level's size
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at the current level
        for _ in range(level_size):
            # Remove the first node from the queue
            node = queue.pop(0)
            
            # Add node to current level 
            current_level.append(node.val)
            
            # Add child nodes to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Reverse the level if needed (alternate direction)
        if not left_to_right:
            current_level.reverse()
        
        # Add level to result and flip traversal direction
        result.append(current_level)
        left_to_right = not left_to_right
    
    return result