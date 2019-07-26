class SequenceIterator:
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step
    
    def __next__(self):
        value = self.current
        self.current += self.step
        return value


if __name__ == "__main__":
    si = SequenceIterator(1, 2)
    seq = [next(si) for _ in range(10)]
    print(seq)
    print(next(si))
    print(next(si))
    print(next(si))
