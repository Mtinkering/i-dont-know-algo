# Operators:
and &
or |
xor ^
not ~
shift left <<
shift right >>
bit tai tri vi bat ky(X >> k) & 1

# AND:
0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

e.g 5 & 6 = 4
00000101
00000110
00000100

# OR
0 & 0 = 0
0 & 1 = 1
1 & 0 = 1
1 & 1 = 1
5 | 6 = 7

# XOR ^
# Does not take care of carry. For example, 1 ^ 1 = 0. The carry is handled by AND in circuits
# So this works together with AND op

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

# XOR voi 0 la giu nguyen, XOR voi 1 la dao lai

# NOT
# Just opposite sign
~ 0 = 1
~ 1 = 0

# shift left
<<: times 2 ^ n

  0 0 0 0 0 1 0 1
shift left  0 0 0 1 0 1 0 0

# shift right
>> chia cho 2 ^ n
  0 0 0 0 0 1 0 1
shift right 0 0 0 0 0 0 0 1


# Get bit
(X >> k) & 1

# Bit manipulation is faster than + - * /

# Bieu dien so dang bu` 2:
TODO: check 45

# Use XOR to get sum:  the sum is small


# Sign and Magitude: not gonna work
# 1's complement: 2 ways to represent zero(we dont want), also need to bring back the carry bit back until it's zero
# 2's complement:
# In Java, compiler represents the signed integers using 2's complement notation.
# The sum of a number and its two's complement is 2^N

# Watch this for number representation: https: // www.youtube.com/watch?v = lKTsv6iVxV4

# Sign and Magitude:
# 1 1 1 1 -7
# 1 1 1 0 -6
# 1 1 0 1 -5
# 1 1 0 0 -4
# 1 0 1 1 -3
# 1 0 1 0 -2
# 1 0 0 1 -1
# 1 0 0 0 -0  ah ha
# 0 0 0 0 0   ah ha
# 0 0 0 1 1
# 0 0 1 0 2
# 0 0 1 1 3
# 0 1 0 0 4
# 0 1 0 1 5
# 0 1 1 0 6
# 0 1 1 1 7
# But to add , for exampe 5 + (-5) using adder, it wont work because of the carry over bit

# Must watch: https://www.youtube.com/watch?v=4qH4unVtJkE

# 1's complement:
# 1 0 0 0

# 2's complement:
# -8 4 2 1: signed bit is the biggest negative integer
# 1 0 0 0
