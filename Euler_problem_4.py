###Problem 4

n = []
for x in range(1,1000):
	for y in range(1,1000):
		a = str(x * y)
		if a == a[::-1]:
			n.append(int(a))
print(max(n))
