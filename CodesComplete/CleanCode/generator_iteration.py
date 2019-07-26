class MappedRange:
    """Apply a transformation to a range of numbers."""

    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wraped = range(start, end)
    
    def __getitem__(self, index):
        value = self._wraped.__getitem__(index)
        result = self._transformation(value)
        print(f"Index {index}: {value}")

        return result
    
    def __len__(self):
        return len(self._wraped) 


if __name__ == '__main__':
    mr = MappedRange(abs, -10, 5)
    print(mr[0])
    print(mr[-1])
    print(list(mr))
    