class NodeType:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinarySearchTreeType:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def inorder_traversal(self):
        self._inorder(self.root)
        print()

    def preorder_traversal(self):
        self._preorder(self.root)
        print()

    def postorder_traversal(self):
        self._postorder(self.root)
        print()

    def tree_height(self):
        return self._height(self.root)

    def tree_node_count(self):
        return self._node_count(self.root)

    def clear_tree(self):
        self._clear(self.root)
        self.root = None

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.info, end=" ")
            self._inorder(node.right)

    def _preorder(self, node):
        if node is not None:
            print(node.info, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.info, end=" ")

    def _clear(self, node):
        if node is not None:
            self._clear(node.left)
            self._clear(node.right)
            del node

    def _height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def _node_count(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._node_count(node.left) + self._node_count(node.right)

    def search(self, item):
        current = self.root
        while current is not None:
            if current.info == item:
                return True
            elif current.info > item:
                current = current.left
            else:
                current = current.right
        return False

    def search_rec(self, item):
        return self._search_rec_priv(self.root, item)

    def _search_rec_priv(self, node, item):
        if node is None:
            return False
        elif node.info == item:
            return True
        elif node.info > item:
            return self._search_rec_priv(node.left, item)
        else:
            return self._search_rec_priv(node.right, item)

    def insert(self, item):
        new_node = NodeType(item)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            trail_current = None
            while current is not None:
                trail_current = current
                if current.info == item:
                    print("The insert item is already in the tree - duplicates are not allowed.")
                    return
                elif current.info > item:
                    current = current.left
                else:
                    current = current.right

            if trail_current.info > item:
                trail_current.left = new_node
            else:
                trail_current.right = new_node

    def remove(self, item):
        if self.root is None:
            print("Cannot delete from the empty tree.")
            return
        if self.root.info == item:
            self._delete_from_tree(self.root)
        else:
            trail_current = self.root
            if self.root.info > item:
                current = self.root.left
            else:
                current = self.root.right
            while current is not None:
                if current.info == item:
                    break
                else:
                    trail_current = current
                    if current.info > item:
                        current = current.left
                    else:
                        current = current.right
            if current is None:
                print("The delete item is not in the tree.")
            elif trail_current.info > item:
                self._delete_from_tree(trail_current.left)
            else:
                self._delete_from_tree(trail_current.right)

    def _delete_from_tree(self, node):
        if node.left is None and node.right is None:
            del node
            node = None
        elif node.left is None:
            temp = node
            node = node.right
            del temp
        elif node.right is None:
            temp = node
            node = node.left
            del temp
        else:
            current = node.left
            trail_current = None
            while current.right is not None:
                trail_current = current
                current = current.right
            node.info = current.info
            if trail_current is None:
                node.left = current.left
            else:
                trail_current.right = current.left
            del current

# Test the class
if __name__ == "__main__":
    b = BinarySearchTreeType()
    b.insert(10)
    b.insert(20)
    b.insert(5)
    b.remove(10)
    b.inorder_traversal()
    b.postorder_traversal()
    b.preorder_traversal()
