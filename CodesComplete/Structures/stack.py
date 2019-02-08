
class Chunk:
    def __init__(self, piece):
        self.piece = piece
        self.next = None


    @property
    def chunk_print(self):
        if self.piece is None:
            return None
        else:
            return self.piece, self.next

    def add(self, piece):
        if self.next is None:
            self.next = Chunk(piece)
        else:
            self.next.add(piece)

    def pop(self):
        if self.next is None:
            self.piece = None
        else:
            self.next.pop()

    def __len__(self):
        if self.piece is None:
            return 0
        elif self.next is None:
            return 1
        else:
            return 1 + len(self.next)

    def __repr__(self):
        return chunk_print

    def __str__(self):
        return chunk_print


class Stack:
    def __init__(self):
        self.content = None

    @property
    def none(self):
        return self.content is None or self.content.piece is None

    def is_empty(self):
        return self.none()

    def add(self, piece):
        if self.content is None:
            self.content = Chunk(piece)
        else:
            self.content.add(piece)

    def push(self, piece):
        self.add(piece)

    def pop(self):
        self.content.pop()

    def stack_print(self):
        if none:
            return
        return print(str(self.content))

    def __str__(self):
        return self.stack_print()

    def __repr__(self):
        return self.stack_print()

    def __len__(self):
        if self.none:
            return 0
        else:
            return len(self.content)


class StackPopException(Exception):
    pass



if __name__ == '__main__':
    stack = Stack()
    assert len(stack) == 0
    stack.push(1)
    assert len(stack) == 1
    print(len(stack))
    stack.pop()
    assert len(stack) == 0
    stack.push(2)
    print(len(stack))
