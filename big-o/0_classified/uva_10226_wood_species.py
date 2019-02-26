
def solve(stat, n):
  for key, val in sorted(stat.items()):
    print(key + ' ' + '%.4f' % (val/n*100))


t = int(input())
input()

for i in range(t):
  species = input()

  stat = {}
  n = 0
  try:
    while species != '':
      n += 1
      stat[species] = stat.get(species, 0) + 1
      species = input()
  except:
    pass
  solve(stat, n)

  if i != t - 1:
    print()
