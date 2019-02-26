# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https: // leetcode.com/problems/subtree-of-another-tree/submissions/


class Solution(object):
  def isSubtree(self, s, t):
    def hashTree(s):
      return "#" + str(s.val) + "$" + hashTree(s.left) + hashTree(s.right) + "@" if s else "^"

    hs = hashTree(s)
    ht = hashTree(t)

    return ht in hs

  def isSubtreehash(self, s, t):

    def hashtree(tree):
      return '^' + str(tree.val) + '#' + hashtree(tree.left) + hashtree(tree.right) if tree else '#'

    hts = hashtree(s)
    htt = hashtree(t)

    return htt in hts

  def isSubtree2(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    def convert(p):
      return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"

    return convert(t) in convert(s)


class Solution3:
  def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    tree = self.hashOfTree(s)
    print tree
    sub = self.hashOfTree(t)
    print sub
    return tree.find(sub) >= 0

  def hashOfTree(self, root):
    hash = ''
    stack = []
    node = root
    while len(stack) > 0 or node:
      while node is not None:
        stack.append(node)
        hash += 'l' + str(node.val)
        node = node.left

      hash += 'ln'
      node = stack.pop()
      hash += 'p' + str(node.val)
      node = node.right
      if not node:
        hash += 'rn'

    return hash


class Solution2(object):
  def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    def isSame(s, t):
      if not s and not t:
        return True
      if (not s and t) or (not t and s) or (s.val != t.val):
        return False

      return isSame(s.left, t.left) and isSame(s.right, t.right)

    if not s:
      return False
    if s.val == t.val and isSame(s, t):
      return True

    return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
