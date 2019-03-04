class Solution2(object):
  def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def dfs(root):
      if root.left:
        dfs(root.left)
      self.ans.append(root.val)
      if root.right:
        dfs(root.right)

    if root == None:
      return []
    else:
      self.ans = []
      dfs(root)
      return self.ans
