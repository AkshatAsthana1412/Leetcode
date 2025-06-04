from binary_tree import Node

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

def inorder_iter(root):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.data)
        node = node.right

def preorder_iter(root):
    stack = []
    node = root
    while stack or node:
        while node:
            print(node.data)
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        node = node.right

def postorder_iter(root):
    pass


        
from collections import deque
def level_order_traversal(root):
    q = deque([root])
    ans = []
    while q:
        level = []
        n = len(q)
        for i in range(n):
            node = q.popleft()
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    nodes = list(map(Node, arr))
    def create_subtree(i, arr):
        root = arr[i]
        n = len(arr)
        if i+1 < n:
            root.left = arr[i+1]
        if i+2 < n:
            root.right = arr[i+2]
        return root
    
    a = create_subtree(3, nodes)
    b = create_subtree(6, nodes)
    root = nodes[0]
    root.left = nodes[1]
    root.right = nodes[2]
    root.left.left = a
    root.right.left = b
    print("Preorder traversal: ")
    preorder_iter(root)
    print(f"Level order traversal: {level_order_traversal(root)}")


