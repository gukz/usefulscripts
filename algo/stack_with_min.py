class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        if val == self.min_stack[-1]:
            self.min_stack = self.min_stack[:-1]
        return val

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(5)
stack.push(4)
stack.push(7)
stack.push(1)
assert stack.get_min() == 1
assert stack.pop() == 1
assert stack.get_min() == 1
assert stack.pop() == 7


def get_max_sum(arr):
    if not arr:
        return None
    end = 0
    res = arr[0]
    cur_sum = 0
    while end < len(arr):
        if arr[end] < 0:
            cur_sum = 0
        else:
            cur_sum += arr[end]
        end += 1
        res = max(res, cur_sum)
    return res


assert get_max_sum([1, 2, -3, 4, 5, -9, -19, 1, 2, 6]) == 9


class TreeRoute:
    def __init__(self):
        self.res = []

    def find(self, tree, target, route):
        if tree is None:
            return
        if tree.val == target and not any((tree.left, tree.right)):
            self.res.append(route)
            return
        self.find(tree.left, target - tree.val, route + [tree])
        self.find(tree.right, target - tree.val, route + [tree])


def is_link_cross(link1, link2):
    link1_set = set()
    p = link1
    end1 = None
    while p is not None:
        if p in link1_set:
            end1 = p
            break
        link1_set.add(p)
        end1 = p
        p = p.next
    p = link2
    end2 = None
    link2_set = set()
    while p is not None:
        if p in link1_set:
            end2 = p
            return True  # 有交叉
        if p in link2_set:
            return False
        link2_set.add(p)
        p = p.next


def is_last_order(arr, min_val, max_val):
    if not arr:
        return True
    head = arr[-1]
    if (min_val is not None and head < min_val) or (
        max_val is not None and head > max_val
    ):
        return False
    index = -1
    for i, v in enumerate(arr):
        if v > head:
            index = i
            break
        if min_val is not None and min_val >= v:
            return False
        if max_val is not None and max_val <= v:
            return False
    if index == -1:
        return is_last_order(arr[:-1], head, max_val)
    return is_last_order(arr[:index], min_val, head) and is_last_order(
        arr[index:-1], head, max_val
    )
    """
       4
    2     6
   1 3   5 7
    """


assert is_last_order([1, 3, 2, 5, 7, 6, 4], None, None) is True


def min_distance(root, node1, node2):
    def get_stack(root, node, cur_stack):
        pass

    stack1 = get_stack(root, node1)
    stack2 = get_stack(root, node2)
    i = 0
    while i < len(stack1) and i < len(stack2):
        if stack1[i] != stack2[i]:
            return len(stack1) + len(stack2) - i * 2
    return abs(len(stack1) - len(stack2))


def find_in_offset(arr, target):
    """递减序列，发生平移"""
    left, right = 0, len(arr) - 1
    split = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[left]:
            right = mid
        elif arr[mid] < arr[right]:
            left = mid
        if right - left < 2:
            if left < len(arr) - 1 and arr[left + 1] > arr[left]:
                split = left
            elif right > 0 and arr[right - 1] > arr[right]:
                split = right
            break

    def bin_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    if split == -1:
        return bin_search(arr, target)

    left = bin_search(arr[: split + 1], target)
    right = bin_search(arr[split + 1 :], target)
    if left == -1:
        if right != -1:
            return split + 1 + right
        return -1
    return left


assert find_in_offset([2, 1, 6, 5, 4, 3], 6) == 2
