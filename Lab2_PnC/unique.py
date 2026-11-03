class Unique:
    def __init__(self, items, **kwargs):
        self.iterator = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __next__(self):
        while True:
            x = next(self.iterator)
            key = x
            if self.ignore_case and isinstance(x, str):
                key = x.upper()
            if key not in self.seen:
                self.seen.add(key)
                return x

    def __iter__(self):
        return self


data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
print(list(Unique(data, ignore_case = True)))
