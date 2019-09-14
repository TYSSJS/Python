l = [1, 2, 3, 4, 5, 6, "hi"]
# slicing
print(l[1:4:2])  # 1- start pnt , 4- end pnt excluding 4th , 2- skip/update
print(l[0:])
print(l[2:len(l)])
l.reverse()
print(l)
print("start to last ", l[:])  # first to last
print("reverse list ", l[:: -1])  # reverse list (:) -> strt pnt (:) -> endpnt
l1=[3,2,4,5,6,"bye"]
print(l1[::-2])
print(l1[-1:1:-2])
print(l1[3::-1])
# # reversing
s="abc"
for i in s[:: -1]:
    print(i, end=" ")
s.replace("a","xyz")
print(s)
print(s.split("a"))

l=[]
for i in range(0,10):
    l.append(i)
print(l)
# list comprehension
print([i for i in range(0, 10)])
print({i for i in range(0, 10)})    # create set
print(set([i for i in range(0, 10)]))  # List comprehension typecast to set



