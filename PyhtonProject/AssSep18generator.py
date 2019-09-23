def a(s):
    n = s
    f = 1
    for i in range(1, n + 1):
        f = f * i
        print(f)
        yield f


for i in a(5):
    print(i)