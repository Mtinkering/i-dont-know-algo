
f[i] = a[i] - i
f[i] - f[i - 1] = a[i] - a[i - 1] - 1 >= 0 -> f asc
f[i] >= f[i - 1]

f[k] = 0

l = 0
r = n - 1  # 3
while l <= r:
  mid = (l + r) // 2  # 1
  if a[mid] - mid == 0:  # a[1] - 1 = -1
    return mid
  if a[mid] - mid < 0:
    l = mid + 1  # l = 2
  else:
    r = mid - 1

print(f([-5, 0, 2, 6]))  # 2
print(f([0, 1, 2, 3]))  # 1
print(f([0, 5, 7, 8]))  # 0


f([-5, 0, 2, 6]) -> [-5, -1, 0, 3]


def transform(root):
  flt_tree = []

  def flatten(node):
    if node is None:
      return
    flatten(node.left)
    flt_tree.append(node)
    flatten(node.right)

  flatten(root)
  # [1,2,7,11,15,29,35,40]
  # [139, asdasd]
  new_value = [0] * len(flt_tree)
  new_value[flt_tree[-1]] = 0
  for i in range(len(flt_tree) - 2, -1, -1):
    new_value[i] = new_value[i + 1] + flt_tree[i + 1].value

  for i in range(len(flt_tree)):
    flt_tree[i].value = new_value
