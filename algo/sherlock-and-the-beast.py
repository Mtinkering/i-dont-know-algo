
# 13/3 = 4 1

# 12 1
# 9 4
# 6 7
# 3 10
# 5553333333333

#!/bin/python



t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    number = "-1"
    if (n%3 == 0):
    	number = "".join(["5" for _ in xrange(n)])
    else:
    	three_of_fives = n//3

    	remaining = n%3 
    	while three_of_fives > -1:
    		if (remaining%5 == 0):
    			break
    		else:
    			three_of_fives -= 1
    			remaining += 3
    	if (three_of_fives != -1):
    		five_of_threes = remaining/5
    		number = "".join(["555" for _ in xrange(three_of_fives)] + ["33333" for _ in xrange(five_of_threes)])

    print number