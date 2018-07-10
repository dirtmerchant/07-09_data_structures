pybites = {'julian': 30, 'bob': 33, 'mike': 33}

print(pybites)
# unordered

people = {}
# empty dictionary

people['julian'] = 30
# assign a key value of 'julian'

print(people)

people['bob'] = 103

print(people)

print(pybites.keys())

print(pybites.values())

print("items")

print("---")
print("keys")
print("---")

for keys in pybites.keys():
	print(keys)

print("---")
print("values")
print("---")

for values in pybites.values():
	print(values)

print("---")
print("keys and values")
print("---")

for keys, values in pybites.items():
	print(keys + str(values))

print("---")
print("keys and values formatted")
print("---")

for keys, values in pybites.items():
	print('%s is %d years of age' % (keys, values))
	

