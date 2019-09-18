# GENERATORS
def genFact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
        yield f
    # return f
    print("hi")
# print(genFact(6))
for i in genFact(6):
    print(i)

    # use of yield
    # we can write statment after yield statement also
    # and no need to create an object
    # yield used only in case, if all the elements need to be printed.

    # use of return
    # after return statement, no more statement can be exceuted
    # end of the block of stmt.
    # object have to be cretated to call the value