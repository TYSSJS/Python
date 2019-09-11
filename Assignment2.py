s="Good Afternoon"
print(s.replace('o','$'))
# replace 'o' with '$'

t="Good Afternoon"
print(t.replace("Good","Bad"))
# replace 'Good' with 'Bad'

# Write script using all the methods in String and list
st="I love Python"

print("Use replace method=",st.replace("I","We"))
print("Use index method=",st.index('o',1))

st1="and Java"
print("@".join(st1))
print(st)

st.split()
print(st)

st2="I love Python"
print(st.find("love"))

print('hi'.startswith('h'))
print('hello'.endswith('o'))
print(' '.isspace())

print("isalnum=",st.isalnum())

print("isalpha=",st.isalpha())

print("title=",st.title())

print("first capital",st.capitalize())

print("Uppercase=",st.isupper())

print("Lower case",st.islower())

print(st.casefold())

# methods using list
li=[1,2,3,5,6,7,8,9,10]
li2=[78,78,96]
li.sort()
print(li)
li.reverse()
print(li)
print(li.index(6))

li1=li.copy()
print(li1)

li.remove(8)
print(li)

print(li.count(9))

li.pop(5)
print(li)

li.extend(li2)
print(li)

li.insert(4,45)
print(li)

li.append('hi')
print(li)

li.clear()
print(li)

