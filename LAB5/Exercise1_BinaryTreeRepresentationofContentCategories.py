class CategoryNode:
    def __init__(self, category_id, name, post_count, parent=None):
        self.category_id = category_id  
        self.name = name  
        self.post_count = post_count  
        self.left = None  
        self.right = None  
        self.parent = parent  

def calculate_height(node):
    if node is None:
        return -1
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

def calculate_node_height(node, target_id):
    target_node = find_category(target_id, node)
    if target_node is None:
        return -1
    return calculate_height(target_node)

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

def is_balanced(node):
    if node is None:
        return True
    
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    
    if abs(left_height - right_height) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True
    return False


def is_full_binary_tree(node):
    if node is None:
        return True
    
    if node.left is None and node.right is None:
        return True
    
    if node.left is not None and node.right is not None:
        return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)
    return False

def is_perfect_binary_tree(node):
    height = calculate_height(node)
    expected_nodes = (2 ** (height + 1)) - 1
    return count_nodes(node) == expected_nodes

def is_complete_binary_tree(node):
    if node is None:
        return True
    queue = [node]
    found_null = False
    
    while queue:
        current = queue.pop(0)
        
        if current is None:
            found_null = True
        else:
            if found_null:
                return False
            queue.append(current.left)
            queue.append(current.right)
            
    return True



def find_category(category_id, node):
    if node is None:
        return None
    if node.category_id == category_id:
        return node
    
    left_result = find_category(category_id, node.left)
    if left_result is not None:
        return left_result
        
    return find_category(category_id, node.right)

def find_path_to_root(category_id, node):
    target = find_category(category_id, node)
    path = []
    
    while target is not None:
        path.append(target.name)
        target = target.parent
        
    return path

def lowest_common_ancestor(id1, id2, node):
    path1 = find_path_to_root(id1, node)
    path2 = find_path_to_root(id2, node)
    
    lca = None
    
    while path1 and path2:
        node1 = path1.pop()
        node2 = path2.pop()
        
        if node1 == node2:
            lca = node1
        else:
            break
            
    return lca