iterable=[1,2,3,4]
itr_obj=iter(iterable)
while True:
    try:
        element=next(itr_obj)
        print(element)
        # element = next(itr_obj)
        # StopIteration
    except StopIteration:
        break
