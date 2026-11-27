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


def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


def is_balanced(node):
    if node is None:
        return True
    if abs(height(node.left) - height(node.right)) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


nums = []
for x in sys.stdin.read().split():
    x = int(x)
    if x == 0:
        break
    nums.append(x)

root = None
for x in nums:
    root = insert(root, x)

print("YES" if is_balanced(root) else "NO")
