# Generic tree node class 
class Node(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  

class Tree(object): 
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key):
        # Step 1 - Perform normal BST 
        if not root:
            print(f"Case #1: Pivot not detected\n{key}")
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
            print(f"Inserted {key} to the left of {root.val}")
        else:
            root.right = self.insert(root.right, key)
            print(f"Inserted {key} to the right of {root.val}")

        # Step 2 - Update the height of the ancestor node 
        root.height = 1 + max(self.calculate_height(root.left), self.calculate_height(root.right))

        # Step 3 - Get the balance factor 
        balance = self.calculate_balance(root)

        if balance > 1 and key < root.left.val: 
            print("Case #3a: adding a node to an outside subtree")
            return self._right_rotate(root) 

        if balance < -1 and key > root.right.val: 
            print("Case #3b: adding a node to an inside subtree")
            return self._left_rotate(root) 

        if balance > 1 and key > root.left.val: 
            if key > root.left.right.val:
                print("Case #3a: adding a node to an outside subtree")
            else:
                print("Case #3b: adding a node to an inside subtree")
            return self._LR_rotate(root) 

        if balance < -1 and key < root.right.val: 
            if key < root.right.left.val:
                print("Case #3a: adding a node to an outside subtree")
            else:
                print("Case #3b: adding a node to an inside subtree")
            return self._RL_rotate(root) 

        print(f"Case #2: A pivot exists, and a node was added to the shorter subtree\nInserted {key} to the right of {root.val}")
        return root 

    def search(self, data):
        if data == self.data:
            return self
        elif data < self.data and self.left is not None:
            return self.left.search(data)
        elif data > self.data and self.right is not None:
            return self.right.search(data)
        else:
            return None

    def _left_rotate(self, z): 
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.calculate_height(z.left), 
                         self.calculate_height(z.right)) 
        y.height = 1 + max(self.calculate_height(y.left), 
                         self.calculate_height(y.right)) 
  
        # Return the new root 
        return y 
  
    def _right_rotate(self, z): 
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.calculate_height(z.left), 
                        self.calculate_height(z.right)) 
        y.height = 1 + max(self.calculate_height(y.left), 
                        self.calculate_height(y.right)) 
  
        # Return the new root 
        return y 
  
    def _LR_rotate(self, z): 
        z.left = self._left_rotate(z.left) 
        return self._right_rotate(z) 
  
    def _RL_rotate(self, z): 
        z.right = self._right_rotate(z.right) 
        return self._left_rotate(z) 
  

    def calculate_height(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def calculate_balance(self, root): 
        if not root: 
            return 0
  
        return self.calculate_height(root.left) - self.calculate_height(root.right) 
  
    def _preorder(self, root):
        if root is not None:
            print(root.key, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
  
 
  
if __name__ =="__main__":
    myTree_1 = Tree() 
    myTree_2 = Tree()

    root_1 = None
    root_2 = None


    print("Test 1:")
    test_1 = [10, 7, 12, 3, 6, 10, 20, 1, 5, 3, 9] # inserting 3 invokes case 3a
    for i in test_1:
        root_1 = myTree_1.insert(root_1, i)

    print("\nTest 2:\n\n")
    test_2 = [30, 20, 40, 35, 50, 45] # case 3b
    for i in test_2:
        root_2 = myTree_2.insert(root_2, i)


