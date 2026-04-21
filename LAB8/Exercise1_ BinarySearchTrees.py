from collections import Counter

class UserNode:
    def __init__(self, user_id, name, friends):
        self.user_id = user_id
        self.name = name
        self.friends = friends
        self.left = None
        self.right = None

class UserBST:
    def __init__(self):
        self.root = None

    def insert(self, user_id, name, friends_list):
        if self.root is None:
            self.root = UserNode(user_id, name, friends_list)
        else:
            self._insert_recursive(self.root, user_id, name, friends_list)

    def _insert_recursive(self, node, user_id, name, friends_list):
        if user_id < node.user_id:
            if node.left is None:
                node.left = UserNode(user_id, name, friends_list)
            else:
                self._insert_recursive(node.left, user_id, name, friends_list)
        elif user_id > node.user_id:
            if node.right is None:
                node.right = UserNode(user_id, name, friends_list)
            else:
                self._insert_recursive(node.right, user_id, name, friends_list)

    def find(self, user_id):
        return self._find_recursive(self.root, user_id)

    def _find_recursive(self, node, user_id):
        if node is None or node.user_id == user_id:
            return node
        
        if user_id < node.user_id:
            return self._find_recursive(node.left, user_id)
        return self._find_recursive(node.right, user_id)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.user_id)
            self._inorder_recursive(node.right, result)

    def delete(self, user_id):
        self.root = self._delete_recursive(self.root, user_id)

    def _delete_recursive(self, node, user_id):
        if node is None:
            return node

        if user_id < node.user_id:
            node.left = self._delete_recursive(node.left, user_id)
        elif user_id > node.user_id:
            node.right = self._delete_recursive(node.right, user_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._get_min(node.right)
            node.user_id = temp.user_id
            node.name = temp.name
            node.friends = temp.friends
            node.right = self._delete_recursive(node.right, temp.user_id)

        return node

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def suggest_friends(self, user_id, max_suggestions=5):
        target_node = self.find(user_id)
        if target_node is None:
            return []

        direct_friends = set(target_node.friends)
        fof_counter = Counter()

        for friend_id in direct_friends:
            friend_node = self.find(friend_id)
            if friend_node is not None:
                for fof_id in friend_node.friends:
                    if fof_id != user_id and fof_id not in direct_friends:
                        fof_counter[fof_id] += 1

        top_fofs = fof_counter.most_common(max_suggestions)
        return [fof_id for fof_id, count in top_fofs]