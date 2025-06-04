from binary_tree import Node
def max_height(root):
    if root is None:
        return 0
    
    return 1 + max(max_height(root.left), max_height(root.right))

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

    print(max_height(root))
