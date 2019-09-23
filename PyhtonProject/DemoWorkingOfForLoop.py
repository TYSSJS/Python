l = [11,52,36,48,19]
for i in l:
    if i%2 == 0:
        print(i)


iterable = [1,2,3,4]
iter_obj = iter(iterable)
while True:
    try:
        element = next(iter_obj)
        print(element, end=" ")
    except StopIteration:
        break
