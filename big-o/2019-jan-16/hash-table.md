<!-- https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1109/ -->

## Hash map:
- Insertion and searching in O(1)

## Hash map principle:
  - Determine the buckets to search
  - Keys go into buckets by hash function

## Hash function:
  - key -> bucket logic
  - The goal is to have uniform
  - Tradeoff between amount of buckets vs the capacity of a bucket


## Collision Resolution
  - If the maxium number of keys in a bucket is not small, consider height-balanced binary search tree instead of array (or linkedlist?)

## Time complexity analysis
  - Using arraylist or dynamic vector, we encounter O(n) when removing an element
  - Instead, we could use
  - 1. linkedlist
  - 2. Another trick is to swap that value to the last one then remove the last one in O(1) => VERY COOL

  - If the size of one bucket is large, instead of using array, we change to height-balanced binary search tree
  - which gives O(logN) for insertion and searching

## Further reading
1. Height-balanced binary search tree