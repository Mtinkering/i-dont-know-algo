n = int(raw_input())

orders = []
for i in range(n):
	t,d = map(int, raw_input().split())
	obj = [t+d,i+1,t]
	orders.append(obj)

sorted_orders = sorted(orders, key = lambda k : (k[0],k[1]))

answer = []
for e in sorted_orders:
	answer.append(str(e[1]))
print " ".join(answer)


# n = input()
# v = []

# for i in range(0, n):
#     a, b = map(int, raw_input().split())
#     v.append((a+b, i+1))
    
# print ' '.join([str(x[1]) for x in sorted(v)])