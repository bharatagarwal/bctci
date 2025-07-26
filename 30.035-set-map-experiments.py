dwarves = [
	"Doc",
	"Grumpy",
	"Happy",
	"Sleepy",
	"Bashful",
	"Sneezy",
	"Dopey",
]

names = set()
details = dict()

details = {
	"Doc": 19,
	"Grumpy": 17,
	"Happy": 12,
	"Sleepy": 21,
	"Bashful": 42,
	"Sneezy": 9,
	"Dopey": 35,
}


for dwarf in dwarves:
	names.add(dwarf)

print(dwarves)

print("set: don't keep order")
for name in names:
	print(name)

print()

print("dict: keep order, iterate over key")
for name, age in details.items():
	print(name, age)

# throws a RuntimeError:
#   dictionary changed size during iteration
# for name in details:
# 	if details[name] < 18:
# 		del details[name]

# throws a TypeError:
#   unhashable type: 'list'
# sum_map = {[1, 2, 3]: 6}

# tuples are immutable
sum_map = {(1, 2, 3): 6}
print(repr(sum_map))
