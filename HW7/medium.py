from logging import root


def search_bst(root, value):
    
    if root is None:
        return False
    if root.value == value:
        return True
    elif value < root.value:
        return search_bst(root.left, value)
    else:
        return search_bst(root.right, value)

# Example usage:
print(search_bst(root, 7))  
print(search_bst(root, 20))  

