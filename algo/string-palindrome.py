




def checkIfPalindrome(s):
	n = len(s)
	middle = n//2

	for i in range(0,middle):
		if (s[i] != s[n-1-i]):
			return False
	return True


for _ in range(0,input()):
	s = raw_input()

	anwser = -1

	n = len(s)
	middle = n//2
	for i in range(0,middle):
		if (s[i] != s[n-1-i]):
			newStr = s[i:n-1-i]
			if checkIfPalindrome(newStr):
				anwser = n-1-i
			else:
				anwser = i
			break

	print anwser


