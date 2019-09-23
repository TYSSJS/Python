try:
    a = [0, 1, 2, 3]
    print(a[5])
except IndexError as i:
    print("uh ho")
    print(i)
except Exception:
    print("from super class")

finally:
    print("it is a finailly block")