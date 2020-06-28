class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 找出树的最小深度
def minDepth(root):
    if root is None:
        return 0
    queue = [(1, root)]
    while queue:
        new_queue = []
        for height, node in queue:
            if node.left is None and node.right is None:
                return height
            if node.left is not None:
                new_queue.append((height + 1, node.left))
            if node.right is not None:
                new_queue.append((height + 1, node.right))
        queue = new_queue
