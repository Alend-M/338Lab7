class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
                return self.left #Return the node you just inserted
            else:
                return self.left.insert(data)  # Recursively insert and return the node
        else:
            if self.right is None:
                self.right = Node(data)
                return self.right # Return the node you just inserted
            else:
                return self.right.insert(data)  # Recursively insert and return the node

    def search(self, data):
        if data == self.data:
            return self
        elif data < self.data and self.left is not None:
            return self.left.search(data)
        elif data > self.data and self.right is not None:
            return self.right.search(data)
        else:
            return None

    def calculate_height(node):
        if node is None:
            return 0
        return 1 + max(calculate_height(node.left), calculate_height(node.right))

    def calculate_balance(node):
        if node is None:
            return 0
        return abs(calculate_height(node.left) - calculate_height(node.right))
    
    def update_balance(self):
        if self is None:
            return
        left_height = self.left.calculate_height() if self.left else 0
        right_height = self.right.calculate_height() if self.right else 0
        self.balance = right_height - left_height

        if abs(self.balance) > 1:
            print("Case #{}: A pivot exists, and a node was added to the shorter subtree".format(2 if self.balance < 0 else 1))
    
    def pivot_check_insert(self, data):
        node, parent = self.insert(data)
        if node is None:
            print("Case #1: Pivot not detected")
        else:
            print("Newly inserted node:", node.data)
            print("Parent node:", parent.data)
            print("Balance of pivot node:", node.calculate_balance())


''' a pivot node is the node where a new node is inserted during the insertion operation'''