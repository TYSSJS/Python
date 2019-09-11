from builtins import print

s = "python for life"
print(s[0: 6])
print(s[7:10])
print(s[11:16])
print(s[2:9])
print(s[8:13])
print()

print(s[0:11]+s[11:16].upper())
print()

print(s[0:7].upper()+s[7:11].lower()+s[11:16].upper())

