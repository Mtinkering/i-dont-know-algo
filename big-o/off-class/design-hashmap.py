# https://leetcode.com/problems/design-hashmap/


class ListNode:
  def __init__(self, key, value):
    self.pair = (key, value)  # If we change to only value, then we get set()
    self.next = None


class MyHashMap:

  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.size = 1000
    self.buckets = [None]*self.size

  def put(self, key, value):
    """
    value will always be non-negative.
    :type key: int
    :type value: int
    :rtype: void
    """
    index = key % self.size

    if self.buckets[index] == None:
      self.buckets[index] = ListNode(key, value)
    else:
      cur = self.buckets[index]

      while True:
        if cur.pair[0] == key:
          cur.pair = (key, value)
          return

        if cur.next == None:
          cur.next = ListNode(key, value)
          return

        cur = cur.next
#           while cur.next != None and cur.pair[0] != key:
#             cur = cur.next

#           if cur.pair[0] == key:
#             cur.pair = (key, value)
#           else:
#             cur.next = ListNode(key, value)

  def get(self, key):
    """
    Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    :type key: int
    :rtype: int
    """
    index = key % self.size

    if self.buckets[index] == None:
      return -1
    else:
      cur = self.buckets[index]

      while True:
        if cur.pair[0] == key:
          return cur.pair[1]

        if cur.next == None:
          return -1

        cur = cur.next

#           while cur.next != None and cur.pair[0] != key:
#             cur = cur.next

#           if cur.pair[0] == key:
#             return cur.pair[1]
#           else:
#             return -1

  def remove(self, key):
    """
    Removes the mapping of the specified value key if this map contains a mapping for the key
    :type key: int
    :rtype: void
    """
    index = key % self.size
    cur = self.buckets[index]

    if cur == None:
      return

    if cur.pair[0] == key:
      self.buckets[index] = cur.next
      cur.next = None
    else:

      prev = cur

      while True:
        if cur.pair[0] == key:
          prev.next = cur.next
          cur.next = None
          return
        if cur.next == None:
          return

        prev = cur
        cur = cur.next


#             while cur.next != None and cur.pair[0] != key:
#               prev = cur
#               cur = cur.next

#             if cur.pair[0] == key:
#               prev.next = cur.next
#               cur.next = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
