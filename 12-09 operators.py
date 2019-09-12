# arithmatic
print(2 + 23)
print(2 - 23)
print(23 - 7)
print(12 * 2)
print(12 / 2)  # 6.0
print(12 % 7)  # reminder 5
print("floor division is ", 45 // 2)  # floor division
print("power is ", 5 ** 2)
print("exponential is ", 5e2)
print((12 * 2 ** 2) / 3)

# logical operator
print(12 > 10)
print(12 < 10)
print(12 == 10)
print(12 != 10)
print(12 >= 10)
print(12 <= 10)

# membership operator
a = [1, 2, 56, 23, 12, 78]
print(54 in a)
print(2 not in a)

# identity operator
a = [1, 2, 3, 4]
print(id(a))  # 2459193660808
b = a
print(id(b))  # 2459193660808
b.append(7)
print(b)  # [1, 2, 3, 4, 7]
print(a)  # [1, 2, 3, 4, 7]
print(b is a)
print(b is not a)
b = [34, 45, 56]
print(b)
print(id(b))  # 2459195108040








