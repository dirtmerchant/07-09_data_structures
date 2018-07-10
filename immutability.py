## Immutability

mystring = 'julian'

l = list(mystring)

t = tuple(mystring)

print(l)
print(t)

l[0] = "t"

print(l)

t[0] = "b"

print(t)

for letter in t:
	print(letter)
	
	
