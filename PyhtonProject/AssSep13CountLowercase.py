s = input("enter string")
a = 0
for i in range(0, len(s)):
    if s[i] >= "a" and s[i] <= "z":
        print(s[i], end=" ")
        a = a + 1

print()
print(a)