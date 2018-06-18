S = list(raw_input())
flag = True
while flag == True:
	flag = False

	for i in xrange(len(S)-1):
		basket = S[i]
		if (S[i] == S[i+1]):
			flag = True
			S[i] = 0
			S[i+1] = 0
	S = [s for s in S if s != 0]

if len(S) == 0:
	print "Empty String"
else:
	print "".join(S)