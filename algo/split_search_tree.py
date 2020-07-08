class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def split(root, target):
    """
        5
    2       8
  1   3   6   9

6
1 root节点，直接返回左右
2 处于某一侧，返回左子树
3 


    """
    if root is None:
        return None, None
    if root.val == target:
        return root.left, root.right
    if root.val < target:
        r_left, r_right = split(root.right, target)
        root.right = r_left
        return root, r_right
    if root.val > target:
        r_left, r_right = split(root.left, target)
        root.left = r_right
        return r_left, root


def print_tree(root):
    if root is None:
        return
    q = [root]
    while q:
        nq = []
        print_val = []
        for e in q:
            print_val.append(e.val)
            if e.left:
                nq.append(e.left)
            if e.right:
                nq.append(e.right)
        q = nq
        print(print_val)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    print_tree(root)
    left, right = split(root, 60)
    print("left")
    print_tree(left)
    print("right")
    print_tree(right)
