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
                self.left.cases_and_balance()
                return self.left
            else:
                #print/return it so that we're 'identifying' the pivot node
                #print(self.left.cases_and_balance())
                return self.left.insert(data)


        else:
            if self.right is None:
                self.right = Node(data)
                self.right.cases_and_balance()
                
                return self.right
            else:
                #print(self.right.cases_and_balance())
                return self.right.insert(data)
  
        

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

        if abs(left_height - right_height) <= 1:
            self.balance = max(left_height, right_height) + 1
            return self
        elif left_height > right_height:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            self.balance = max(left_height, right_height) + 1
            return self
        elif left_height < right_height:
            print("Case 3 not supported")

        else:
            print("Case #1: Pivot not detected")
            self.balance = max(left_height, right_height) + 1
        
        return self


def calculate_height(node):
    if node is None:
        return 0
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

def calculate_balance(node):
    if node is None:
        return 0
    return abs(calculate_height(node.left) - calculate_height(node.right))

''' a pivot node is the node where a new node is inserted during the insertion operation'''
#Main code:

root = Node(10)
print("Initial Tree:")
print("Root:", root.data)

print("\nTest Case 1")
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
# No pivot node exists
print("\nTest Case 2")
root.insert(2)
# Node 2 is inserted into the shorter subtree (left subtree of 3)
print("\nTest Case 3")
root.insert(20)
# Node 20 is inserted into the longer subtree (right subtree of 15)

