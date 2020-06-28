class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def snake_print(root):
    if root is None:
        return
    line = [root]
    line_index = 0
    while line:
        new_line = []
        print_val = []
        for l in line:
            print_val.append(l.val)
            if l.left:
                new_line.append(l.left)
            if l.right:
                new_line.append(l.right)
        line = new_line
        line_index = line_index % 2
        if line_index == 1:
            print_val = print_val[::-1]
        line_index += 1
        print(print_val)


if __name__ == "__main__":
    node = Node(1)
    node.left = Node(3)
    node.right = Node(2)
    node.left.left = Node(5)
    node.left.right = Node(4)
    node.right.left = Node(8)
    node.right.right = Node(3)
    snake_print(node)
