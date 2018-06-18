

for _ in xrange(int(raw_input())):
	n,threshold = map(int, raw_input().split())

	late = [int(x) for x in raw_input().split() if int(x) > 0 ]
	if (n - len(late) < threshold ):
		print "YES"
	else:
		print "NO"
