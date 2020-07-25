class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_ele(root, ele):
    head = Node(0)
    head.next = root
    p = head
    while p.next is not None:
        if p.next.val == ele:
            p.next = p.next.next
        else:
            p = p.next
    return head.next


def remove_dup_ele(root):
    p = root
    while p is not None and p.next is not None:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return root


def print_list(root):
    res = []
    p = root
    while p is not None:
        res.append(p.val)
        p = p.next
    print(res)


root = Node(1)
root.next = Node(3)
root.next.next = Node(2)
print_list(remove_ele(root, 1))
root = Node(1)
root.next = Node(3)
root.next.next = Node(3)
print_list(remove_dup_ele(root))
