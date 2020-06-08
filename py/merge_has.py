class MergeFind:
    def __init__(self, temp):
        self.temp = temp

    def find(self, val):
        if self.temp[val] == val:
            return val
        res = self.find(self.temp[val])
        self.temp[val] = res
        return res

    def merge(self, a, b):
        f1, f2 = self.find(a), self.find(b)
        self.temp[f1] = f2
