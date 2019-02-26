# https: // leetcode.com/explore/learn/card/hash-table/182/practical-applications/1142/


class ListNode:
  def __init__(self, value):
    self.key = value


class MyHashSet:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.size = 1000
    self.buckets = [None]*self.size

  def add(self, key):
    """
    :type key: int
    :rtype: void
    """
    if self.contains(key):
      return

    index = key % self.size

    if self.buckets[index] == None:
      self.buckets[index] = [key]
    else:
      self.buckets[index].append(key)

  def remove(self, key):
    """
    :type key: int
    :rtype: void
    """
    index = key % self.size

    if self.buckets[index] == None:
      return

    idx = -1
    for i, v in enumerate(self.buckets[index]):
      if v == key:
        idx = i

    if idx != -1:
      del self.buckets[index][idx]

  def contains(self, key):
    """
    Returns true if this set contains the specified element
    :type key: int
    :rtype: bool
    """
    index = key % self.size

    if self.buckets[index] == None:
      return False
    else:
      for v in self.buckets[index]:
        if v == key:
          return True
      return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
