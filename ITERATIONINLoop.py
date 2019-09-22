l2=[11,52,36,48,19]
for i in l2:
    if i%2==0:
        print(i)


iterable=[1,2,3,4]
iter_element=iter(iterable)
while True:
    try:
        element=next(iter_element)
        print(element)
    except StopIteration:
        break



