# https: // www.hackerrank.com/challenges/cipher/problem
def cipher(k, s):
  n = len(s) - k + 1
  decoded = []

  for i in range(n):
    c = int(s[i])
    bit = c
    if i < k:
      if i != 0:
        bit = int(s[i-1]) ^ c
    else:
      bit = int(s[i-1]) ^ decoded[i-k] ^ c

    decoded.append(bit)

  return ''.join(map(str, decoded))
