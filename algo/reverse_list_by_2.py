class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_first_n(node, n):
    res = Node(0)
    p = node
    for i in range(n):
        if p is not None:
            p_next = p.next
            p.next = res.next
            res.next = p
            p = p_next
        else:
            break
    return res.next, p


def reverse_by_2(root):
    head = None
    tail = root
    last = None
    while tail is not None:
        temp, tail = reverse_first_n(tail, 2)
        if head is None:
            head = temp
            last = head
        else:
            last.next = temp
        while last.next is not None:
            last = last.next
    return head


if __name__ == "__main__":
    # 1 3 2 4 5
    root1 = Node(1)
    root1.next = Node(3)
    root1.next.next = Node(2)
    root1.next.next.next = Node(4)
    root1.next.next.next.next = Node(5)
    # 3 1 4 2 5
    res = reverse_by_2(root1)
    assert res.val == 3
    assert res.next.val == 1
    assert res.next.next.val == 4
    assert res.next.next.next.val == 2
    assert res.next.next.next.next.val == 5
