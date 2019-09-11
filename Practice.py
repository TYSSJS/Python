i=54
j=76
k=82
sum=(i+j)
print("the sum of {0},{1} is {2}".format(i, j, sum))
# if(i>j) and (i>k):
#         print("greater number is",i)
#         elif(j>i)and(j>k):
#             print("greater number is",j)
#         else:
#         print("greater number is",k)

if (i>= j) and (i >= k):
   largest = i
elif (j >= i) and (j >= k):
   largest = j
else:
   largest = k

print("The largest number between",i,",",j,"and",k,"is",largest)