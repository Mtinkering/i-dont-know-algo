#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#


class Node():
  def __init__(self):
    self.child = {}
    self.numChild = 0


def addNode(root, word):
  cur = root

  for c in word:
    if c not in cur.child:
      cur.child[c] = Node()

    cur = cur.child[c]
    cur.numChild += 1


def findNode(root, partial):
  cur = root

  for c in partial:
    if c not in cur.child:
      return 0

    cur = cur.child[c]

  return cur.numChild


def contacts(queries):
  root = Node()
  res = []

  for op, string in queries:
    if op == 'add':
      addNode(root, string)
    else:
      res.append(findNode(root, string))

  return res


if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  queries_rows = int(input())

  queries = []

  for _ in range(queries_rows):
    queries.append(input().rstrip().split())

  result = contacts(queries)

  fptr.write('\n'.join(map(str, result)))
  fptr.write('\n')

  fptr.close()
