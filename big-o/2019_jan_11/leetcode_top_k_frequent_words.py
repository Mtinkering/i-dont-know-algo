# https: // leetcode.com/problems/top-k-frequent-words/submissions/

import queue


class Node():
  def __init__(self, item):
    self.key = item[0]
    self.freq = item[1]

  def __lt__(self, other):
    if self.freq == other.freq:
      return self.key > other.key

    return self.freq < other.freq


class Solution:
  def topKFrequent(self, words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    d = {}
    minHeap = queue.PriorityQueue()

    for word in words:
      if word not in d:
        d[word] = 0
      d[word] += 1

    # items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    for item in d.items():
      if len(minHeap.queue) >= k:
        top = minHeap.queue[0]
        if item[1] < top.freq or (item[1] == top.freq and item[0] >= top.key):
          continue

        minHeap.get()

      minHeap.put(Node(item))

    s = []
    while len(minHeap.queue) != 0:
      s.append(minHeap.get().key)

    s.reverse()
    return s
