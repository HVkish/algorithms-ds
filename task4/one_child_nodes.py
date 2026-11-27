import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


def walk(node, res):
    if node is None:
        return
    walk(node.left, res)
    if (node.left is None) != (node.right is None):
        res.append(node.val)
    walk(node.right, res)


nums = []
for x in sys.stdin.read().split():
    x = int(x)
    if x == 0:
        break
    nums.append(x)

root = None
for x in nums:
    root = insert(root, x)

res = []
walk(root, res)
print(*res)
