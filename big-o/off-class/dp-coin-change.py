#!/bin/python3

import math
import os
import random
import re
import sys


nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'

dp = [0]*(n+1)


def getState(n, c):
  if n < 0:
    return 0
  if n == 0:
    return 1

  if n in dp:
    return dp[n]

  for ci in c:
    dp[n] += getState(n-ci, c)

  return dp[n]


ways = getState(n, c)
print(dp)
print(ways)
