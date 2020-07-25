class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_nodes(node):
    if not node:
        return
    queue = [node]
    while queue:
        next_queue = []
        print_val = []
        for element in queue:
            print_val.append(element.val)
            if element.left:
                next_queue.append(element.left)
            if element.right:
                next_queue.append(element.right)
        queue = next_queue
        print(print_val)


def dump(root):
    """
    树的前序遍历结果、中序遍历结果
    """

    def pre_order(node, cur):
        if not node:
            return
        cur.append(node.val)
        pre_order(node.left, cur)
        pre_order(node.right, cur)

    def mid_order(node, cur):
        if not node:
            return
        pre_order(node.left, cur)
        cur.append(node.val)
        pre_order(node.right, cur)

    res1 = []
    pre_order(root, res1)
    res2 = []
    mid_order(root, res2)
    print(res1)
    print(res2)


node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.left = Node(6)
node.right.right = Node(7)
dump(node)


def load(arr):
    pass
