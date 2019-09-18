itr=[1,2,3,4,5]
itr_obj=iter(itr)
while True:
    try:

        el=next(itr_obj)
        print(el)
    except StopIteration:
        break
