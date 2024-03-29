

# ''' a pivot node is the node where a new node is inserted during the insertion operation'''


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

    def cases_and_balance(self):
        left_height = calculate_height(self.left)
        right_height = calculate_height(self.right)

        if (left_height - right_height) == 0:
            print("Case #1: Pivot not detected:")
            self.balance = max(left_height, right_height) + 1  #max() finds the largest value btwn the arguments, returns r or l, whichever is higher
            return self

        elif left_height - right_height == 1:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree:")
            self.balance = max(left_height, right_height) + 1
            return self

        elif left_height - right_height == -1:
            print("Case 3 not supported:")
            self.balance = max(left_height, right_height) + 1
            return self

        else:
            return self

def calculate_height(node):
    if node is None:
        return 0
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

def calculate_balance(node):
    if node is None:
        return 0
    return abs(calculate_height(node.left) - calculate_height(node.right))


if __name__ == "__main__":
    root = Node(10)

    #Implement 4 Test Cases:

    # Adding a node that results in Case 1:
    test_1 = [5,15,4]
    for i in test_1:
        root.cases_and_balance()
        root.insert(i)

    # Adding a node that results in Case 2:
    test_2 = [3,20]
    for i in test_2:
        root.cases_and_balance()
        root.insert(i)
        

    # Adding a node that results in Case 3 (on the last one)
    test_3 = [21,22,23]
    for i in test_3:
        root.cases_and_balance()
        root.insert(i)
  




'''Output: 

Case #1: Pivot not detected:
Inserted 5 to the left of 10
Case #2: A pivot exists, and a node was added to the shorter subtree:
Inserted 15 to the right of 10
Case #1: Pivot not detected:
Inserted 4 to the left of 5
Case #2: A pivot exists, and a node was added to the shorter subtree:
Inserted 3 to the left of 4
Inserted 20 to the right of 15
Case #2: A pivot exists, and a node was added to the shorter subtree:
Inserted 21 to the right of 20
Case #1: Pivot not detected:
Inserted 22 to the right of 21
Case 3 not supported:
Inserted 23 to the right of 22

'''


