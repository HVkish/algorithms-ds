n = int(input())
a = list(map(int, input().split()))

res = [-1] * n
stack = []
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    if stack:
        res[i] = stack[-1]
    stack.append(i)

print(*res)
