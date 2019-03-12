def f2(a):
    global b
    print(a)
    print(b)
    b = 9
    print(b)


b = 5
f2(3)