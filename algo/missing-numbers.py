n = int(raw_input())

results = [0]*201


array  = [int(x) for x in raw_input().split()]
base = array[0]

for i in array:
	j = i - base + 100
	results[j] += 1

m = int(raw_input())

for y in raw_input().split():
	k = int(y) - base + 100
	results[k] += -1
output = []
print results
for i in range(0,201):
	if (results[i] < 0):
		output.append(i+base -100)


print " ".join(map(str,output))