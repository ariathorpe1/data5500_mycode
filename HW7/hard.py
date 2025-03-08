# Deleting a node from a Binary Search Tree (BST) involves three main cases:

# 1. **Deleting a leaf node (no children):**
#    - Simply remove the node from the tree by setting its parent’s pointer to None.

# 2. **Deleting a node with one child:**
#    - Replace the node with its only child by updating the parent’s pointer to refer to the child.

# 3. **Deleting a node with two children:**
#    - Find the node’s in-order successor (smallest node in the right subtree) or in-order predecessor (largest in the left subtree).
#    - Replace the node’s value with the successor/predecessor’s value.
#    - Recursively delete the successor/predecessor.

### Challenges & Edge Cases:
# - **Tree Imbalance:** Removing nodes can make a BST unbalanced, potentially degrading search performance to O(n). Using self-balancing trees (e.g., AVL or Red-Black Trees) can help.
# - **Handling root deletion:** If the root node is deleted, extra care is needed to update the root reference.
# - **Recursive vs Iterative Implementation:** Recursive solutions are cleaner but could cause stack overflow for very deep trees. Iterative approaches avoid this but require additional logic.

### Python Implementation (Deletion Function):

def delete_node(root, value):
    if root is None:
        return root
    
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        temp = get_min(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    
    return root

# Helper function to get the smallest node in a subtree
def get_min(node):
    while node.left is not None:
        node = node.left
    return node

#This function correctly handles all deletion cases and ensures the BST structure remains valid.

