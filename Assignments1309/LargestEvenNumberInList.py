l = [1, 2, 5, 4, 3]
l.sort()
i = len(l) - 1
while i >= 0:
    if l[i] % 2 == 0:
        print(l[i])
        break
    i -= 1
