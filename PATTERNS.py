# for i in range(0,6):
#     for j in range(0,i):
#         print("*",end= " ")   #
#     print(" ")

# o/p
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *

# for i in range(5):
#     num=1
#     for j in range(0,i):
#         print(num,end= " ")
#         num += 1
#     print(" ")

# o/p
#   1
#   1 2
#   1 2 3
#   1 2 3 4
#
num = 1
for i in range(5):

    for j in range(0, i):
        print(num, end=" ")
        num += 1
    print(" ")

#  o/p
#   1
#   2 3
#   4 5 6
#   7 8 9 10


for i in range(5):
    n = ['A','B','C','D']
    for j in range(0, i):
        print(n[j], end=" ")

    print(" ")


for i in range(5):
    n = 65
    for j in range(0, i):
        print(chr(n), end=" ")
        n=n+1

    print(" ")

#   A
#   A B
#   A B C
#   A B C D


num=0
for  i in range(5):
    for j in range(0,i):
        print(num,end= " ")
    num += 1
    print(" ")

#   1
#   2 2
#   3 3 3
#   4 4 4 4

# num=0
# for  i in range(5):
#     for j in range(5):
#         print(num,end= " ")
#     num += 1
#     print(" ")

#   1 1 1 1 1
#   2 2 2 2 2
#   3 3 3 3 3
#   4 4 4 4 4

print(" ")

for  i in range(5):
    for j in range(5):
        if i+j<=6//2:
            print("*",end=" ")
        else:
            print("$",end=" ")
    print(" ")

#   * * * * $
#   * * * $ $
#   * * $ $ $
#   * $ $ $ $
#   $ $ $ $ $


# def p1(n):
#     k=2*n-2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end=" ")
#         k=k-1
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print(" ")
# p1(5)
# print(" ")


def p1(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print(k,end=" ")
        print(" ")

p1(5)
print(" ")
