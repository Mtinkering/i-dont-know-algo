
A,B,N = [int(x) for x in raw_input().split()]

def fib_m(a,b,n):
	fib = [0]*n
	fib[0] = a
	fib[1] = b

	for i in range(2,n):
		fib[i] = fib[i-1]*fib[i-1] + fib[i-2]

	return fib[-1]


print fib_m(A,B,N)