def bSort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

a = [5, 6, 2, 4, 8]
bSort(a)
for i in range(len(a)):
    print(a[i], end=" ")
