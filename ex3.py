

# ''' a pivot node is the node where a new node is inserted during the insertion operation'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.balance = 0
        self.parent = None

    def insert(self, data):
    
        if data <= self.data:
            if self.left is None:
                self.left = Node(data, parent=self)  # Pass self as the parent
                print(f"Inserted {data} to the left of {self.data}")
                self.update_balances_upwards(self.left)

            else: # Outside subtree on the right of the left child
                if data <= self.left.data:  # Outside subtree on the left of the left child
                    self.left.left = Node(data, parent=self.left)  # Pass self.left as the parent
                    print(f"Inserted {data} to the left of {self.left.data}")
                    print("Case #3a: adding a node to an outside subtree ^")
                    self.update_balances_upwards(self.left.left)

                else:  # Outside subtree on the right of the left child
                    if data <= self.left.right.data:  # Inside subtree of the son of the pivot
                        print("Case 3b not supported")
                    else:
                        self.left.right = Node(data, parent=self.left)  # Pass self.left as the parent
                        print(f"Inserted {data} to the right of {self.left.data}")
                        print("Case #3a: adding a node to an outside subtree^")
                        self.update_balances_upwards(self.left.right)
        else:
            if self.right is None:
                self.right = Node(data, parent=self)  # Pass self as the parent
                print(f"Inserted {data} to the right of {self.data}")
                self.update_balances_upwards(self.right)
            else:
                if data <= self.right.data:  # Outside subtree on the left of the right child
                    if self.right.left is not None:  # Inside subtree of the son of the pivot
                        print("Case 3b not supported")
                    else:
                        self.right.left = Node(data, parent=self.right)  # Pass self.right as the parent
                        print(f"Inserted {data} to the left of {self.right.data}")
                        print("Case #3a: adding a node to an outside subtree^")
                        self.update_balances_upwards(self.right.left)

                else:  # Outside subtree on the right of the right child
                    self.right.right = Node(data, parent=self.right)  # Pass self.right as the parent
                    print(f"Inserted {data} to the right of {self.right.data}")
                    print("Case #3a: adding a node to an outside subtree^")
                    self.update_balances_upwards(self.right.right)

    def search(self, data):
        if data == self.data:
            return self
        elif data < self.data and self.left is not None:
            return self.left.search(data)
        elif data > self.data and self.right is not None:
            return self.right.search(data)
        else:
            return None

    def cases_and_balance(self):
        left_height = calculate_height(self.left)
        right_height = calculate_height(self.right)

        if (left_height - right_height) == 0:
            print("Case #1: Pivot not detected:\n")
            self.balance = max(left_height, right_height) + 1  #max() finds the largest value btwn the arguments, returns r or l, whichever is higher
            return self

        elif left_height - right_height == 1:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree:\n")
            self.balance = max(left_height, right_height) + 1
            return self

        elif left_height - right_height == -1:
            print("Case #3: A pivot exists, and a node was added to the longer subtree:\n")
            return self

        else:
            return self

    # Function to perform left rotation
    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    
    def update_balances_upwards(self, node):
        if node is None:
            return
        node.balance = calculate_balance(node)
        if node.balance < -1 or node.balance > 1:
            print(f"Balance updated for node {node.data}: {node.balance}")
        if node.parent:
            self.update_balances_upwards(node.parent)

def calculate_height(node):
    if node is None:
        return 0
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

def calculate_balance(node):
    if node is None:
        return 0
    return abs(calculate_height(node.left) - calculate_height(node.right))


if __name__ == "__main__":
    
    root_1 = Node(10)

    # Test Case 3a: Adding nodes to create Case 3a scenario
    print("BST after Test Case 3a:")
    test_data_1 = [5, 15, 12, 20, 25]  # Creating a right outside subtree
    for i in test_data_1:
        root_1.insert(i)
        root_1.cases_and_balance()



    root_2 = Node(10)

    # Test Case 3b: Adding nodes to create Case 3b scenario
    test_data_2 = [5, 15, 12, 17, 20]  # Creating a Case 3b scenario
    for i in test_data_2:
        root_2.insert(i)
        root_2.cases_and_balance()


