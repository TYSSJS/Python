s1="python is scripting language"

# To capitalise first letter of the string
print(s1.capitalize())
#o/p--Python is scripting language

# To capitalise first letter of each words of the string
print(s1.title())
#o/p--Python Is Scripting Language

print("hi".isupper())
#o/p-->False


print(s1.islower())
#o/p-->True

print(" ".isspace())
#o/p-->True

print("Annapurna".startswith("A"))
#o/p-->True

print("Annapurna".endswith("l"))
#o/p-->False


print(s1.isalpha())
#o/p-->False


print("abc123".isnumeric())
#o/p-->False

a="world wide web"
print(a.count("w"))   #o/p-->3
print(a.count("w",3))    #o/p-->2
print(a.count("w",6,10))   #o/p-->1
print(a.index("w",6,10))  #O/P-->6
print(a.index("w",5))       #O/P-->6
print(a.index("w"))        #O/P-->0
print(a.index("web"))       #O/P-->11
print(a.replace("web","focus"))  #o/p--> world wide focus
print(a.__add__(" available"))      #o/p--> world wide web available

print(a.split(" ")) #['world', 'wide', 'web']
print(a.split("w")) # ['', 'orld ', 'ide ', 'eb']
print(a.split("o")) #['w', 'rld wide web']

print(a.split("e")) #['world wid', ' w', 'b']
print(a.split("w",2))  #'', 'orld ', 'ide web']
print("annapurna".split("a",3))  #['', 'nn', 'purn', '']
print("annapurna".split("n",2))  #['a', '', 'apurna']

print("abc".join("xyz"))  #xabcyabcz


z=a.split(" ")
print(" @ ".join(z))   # world @ wide @ web
