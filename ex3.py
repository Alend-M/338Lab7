# ex3.py

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        self.balance = 0

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def insert_helper(node, data):
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = insert_helper(node.left, data)
            else:
                node.right = insert_helper(node.right, data)
            node.balance = max(calculate_height(node.left), calculate_height(node.right)) + 1
            balance = calculate_balance(node)
            if balance > 1:
                if data < node.left.data:
                    return self._right_rotate(node)
                else:
                    print("Case 3a: adding a node to an outside subtree")
                    node.left = self._left_rotate(node.left)
                    return self._right_rotate(node)
            elif balance < -1:
                if data > node.right.data:
                    return self._left_rotate(node)
                else:
                    print("Case 3b not supported.")
                    return self._right_rotate(node)
            return node
        self.root = insert_helper(self.root, data)

    def search(self, data):
        if data == self.data:
            return self
        elif data < self.data and self.left is not None:
            return self.left.search(data)
        elif data > self.data and self.right is not None:
            return self.right.search(data)
        else:
            return None
    
    def _left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(calculate_height(x.left), calculate_height(x.right))
        y.height = 1 + max(calculate_height(y.left), calculate_height(y.right))

        return y

    def _right_rotate(self, x):
        y = x.left
        t2 = y.right

        y.right = x
        x.left = t2

        x.height = 1 + max(calculate_height(x.left), calculate_height(x.right))
        y.height = 1 + max(calculate_height(y.left), calculate_height(y.right))

        return y

def calculate_height(node):
    if node is None:
        return 0
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

def calculate_balance(node):
    if node is None:
        return 0
    return calculate_height(node.left) - calculate_height(node.right)


if __name__ == "__main__":
    tree = Tree()
    nodes = [10, 7, 12, 3, 6, 10, 20, 1, 5, 3, 9] # inserting 3 invokes case 3a
    for data in nodes:
        tree.insert(data)