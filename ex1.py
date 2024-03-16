import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
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

def calculate_height(node):
    if node is None:
        return 0
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

def calculate_balance(node):
    if node is None:
        return 0
    return abs(calculate_height(node.left) - calculate_height(node.right))

# Generate 1000 random search tasks
integers_list = list(range(1, 1001))
search_tasks = [random.sample(integers_list, len(integers_list)) for _ in range(1000)]

search_times = []
max_balances = []

for task in search_tasks:
    root = Node(task[0])  # Initialize the tree with the first element of each task
    for num in task[1:]:
        root.insert(num)  # Insert all other elements into the tree
    
    start_time = timeit.default_timer()
    for num in integers_list:
        root.search(num)  # Search for each integer in the tree
    search_times.append(timeit.default_timer() - start_time)

    # Measure maximum balance in the tree
    max_balance = 0
    queue = [root]
    while queue:
        node = queue.pop(0)
        balance = calculate_balance(node)
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
