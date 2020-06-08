class Stack:
    def __init__(self):
        self.queue = []

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        if not self.queue:
            return None
        #
        temp_queue = []
        while len(self.queue) > 1:
            temp_queue.append(self.queue[0])
            self.queue = self.queue[1:]
        res = self.queue[-1]
        self.queue = temp_queue
        #
        return res


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if not self.stack1:
            return None

        while len(self.stack1) > 1:
            self.stack2.append(self.stack1[-1])
            self.stack1 = self.stack1[: len(self.stack1) - 1]
        res = self.stack1[-1]
        self.stack1 = []
        while self.stack2:
            self.stack1.append(self.stack2[-1])
            self.stack2 = self.stack2[: len(self.stack2) - 1]
        return res
