class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


if __name__ == '__main__':
    f = Foo()
    for i in f: print(i)

    print(20 in f)
    print(30 in f)
    print(25 in f)
