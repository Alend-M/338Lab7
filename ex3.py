# ex3.py

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.balance = 0

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
                print(f"Inserted {data} to the left of {self.data}")
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
                print(f"Inserted {data} to the right of {self.data}")
            else:
                self.right.insert(data)

    def search(self, data):
        if data == self.data:
            return self
        elif data < self.data and self.left is not None:
            return self.left.search(data)
        elif data > self.data and self.right is not None:
            return self.right.search(data)
        else:
            return None

    def cases_and_balance(self, root, data):
        left_height = calculate_height(self.left)
        right_height = calculate_height(self.right)

        if (left_height - right_height) == 0:
            print("Case #1: Pivot not detected:")
            self.insert(data)
            self.balance = max(calculate_height(self.left), calculate_height(self.right)) + 1  #max() finds the largest value btwn the arguments, returns r or l, whichever is higher
            return self

        elif (left_height - right_height) == 1:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree:")
            self.insert(data)
            self.balance = max(calculate_height(self.left), calculate_height(self.right)) + 1
            return self

        elif (left_height - right_height) > 1 and (data < root.left.data):
            print("Case 3a: adding a node to an outside subtree")
            self.insert(data)
            self._right_rotate()
            return self
        else: 
            print("Case 3b not supported")
            return self
    
    def _left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _right_rotate(self, x):
        y = x.left
        t2 = y.right

        y.right = x
        x.left = t2

        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

def calculate_height(node):
    if node is None:
        return 0
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

def calculate_balance(node):
    if node is None:
        return 0
    return abs(calculate_height(node.left) - calculate_height(node.right))


if __name__ == "__main__":
    tree = Node(0)
    root = None

    root = tree.cases_and_balance(root, 10) # case 1
    root = tree.cases_and_balance(root, 25) # case 3b