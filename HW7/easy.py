class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_into_bst(root, value):
   
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

# Example usage:
root = TreeNode(10)
insert_into_bst(root, 5)
insert_into_bst(root, 15)
insert_into_bst(root, 2)
insert_into_bst(root, 7)



