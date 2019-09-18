print("Question no.17(a)")
for i in range(6):
    for j in range(0,i):
        print("*", end=' ')
    print()
# pattern program
# *
# * *
# * * *
# * * * *
# * * * * *

print("Question no.17(b)")
for a in range(5):
    num=1
    for b in range(a):
        print(num, end=' ')
        num+=1
    print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4


print("Question no.17(c)")
for m in range(5):
    for n in range(m):
        print(m,end=' ')
    print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4

print("Question no.17(d)")
for k in range(5):
    for l in range(0,5):
        print("*", end=' ')
    print(" ")
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

print("Question no.17(e)")
for i in range(5):
    num=1
    for i in range(0,5):
        print(num,end=' ')
        num+=1
    print(" ")
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

print("Question no.17(f)")
for i in range(1,5):
    for j in range(0,5):
        print(i, end=' ')
    print(" ")
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4

print("Question no.17(g)")
for i in range(5):
    k=65
    for j in range(0,i):
        print(chr(k),end=' ')
        k+=1
    print(" ")
# A
# A B
# A B C
# A B C D

print(" ")
i=65
print("print a character using chr:",chr(i))

print("Question no.17(h)")
num=1
for i in range(5):
    for j in range(0,i):
        print(num,end=' ')
        num+=1
    print(" ")
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# print("---pascal triangle---")
# def p1(n):
#     k=2*n-2
#     for i in range(0,n):
#         for j in range(0,k):
#             print(end='')
#         k=k-1
#     for j in range(0,i+1):
#             print(n,end='')
#             print()
# p1(5)
