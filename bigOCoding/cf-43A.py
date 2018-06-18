teamA = ''
teamB = ''
scoreA = 0
scoreB = 0
for i in range(int(input())):
  team = input().strip()
  if i == 0:
    teamA = team
    scoreA = 1
  elif teamA == team:
    scoreA += 1
  else:
    scoreB += 1
    teamB = team

print(teamA if scoreA > scoreB else teamB)
