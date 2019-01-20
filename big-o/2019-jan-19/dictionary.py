# https: // icpcarchive.ecs.baylor.edu/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 3803
def solve(p, s):
  portu = []
  nol = []

  for i in range(p):
    portu.append(input())

  for i in range(s):
    nol.append(input())

  counter = 0
  words = set()

  for pword in portu:
    for k in range(1, len(pword)+1):
      psub = pword[:k]

      for sword in nol:
        for l in range(0, len(sword)):
          ssub = sword[l:]

          newWord = psub + ssub

          if newWord not in words:
            counter += 1
            words.add(newWord)

  print(counter)


def main():
  p, s = map(int, input().split())

  while p != 0 or s != 0:
    solve(p, s)
    p, s = map(int, input().split())


main()
