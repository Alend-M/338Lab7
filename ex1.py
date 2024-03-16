import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = 0

    def calculate_balance(self):
        return abs(self.calculate_height(self.left) - self.calculate_height(self.right))

    def calculate_height(self, node):
        if node is None:
            return 0
        return 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))

    def insert(self, data, root=None):
        current = root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        newnode = Node(data, parent)    
        if root is None:
            root = newnode
        elif data <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode
        return newnode

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    
    def preorder(self, root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    def search(self, data, root=None):
        current = root if root else self
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None


#change back to 1001 
integers_list = [random.randint(0, 1000) for _ in range(1000)]

#Change it back to 1000
search_tasks = [random.sample(integers_list, len(integers_list)) for _ in range(1000)]

search_times = []
max_balances = []

root = Node(integers_list[0])
for task in search_tasks:
    for num in integers_list[1:]:
        node = root.insert(num)
    start_time = timeit.default_timer()
    for num in task:
        root.search(num)
    search_times.append(timeit.default_timer() - start_time)

#TODO: FIX the measure the balance please and thank you alend
    # Measure balance for each node
    max_balance = 0
    queue = [root]
    while queue:
        node = queue.pop(0)
        balance = node.calculate_balance()
        if balance > max_balance:
            max_balance = balance
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    max_balances.append(max_balance)

# Generate scatterplot
plt.scatter(max_balances, search_times, alpha=0.5)
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time (s)')
plt.title('Absolute Balance vs. Search Time')
plt.show()
