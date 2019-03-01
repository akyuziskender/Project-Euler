###Problem 20

total = 1

for num in range(1,101):
	total = total * num

a = str(total)

sum = 0
for char in a:
	sum += int(char)

print(sum)
