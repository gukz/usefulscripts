class Node:
    def __init__(self, v):
        self.v = v
        self.next = None


def reverse_list(root):
    p = root
    head = Node(0)
    while p is not None:
        p_next = p.next
        p.next = head.next
        head.next = p
        p = p_next
    return head.next


if __name__ == "__main__":
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(3)

    reversed_list1 = reverse_list(list1)
    print(reversed_list1.v)
    print(reversed_list1.next.v)
    print(reversed_list1.next.next.v)
