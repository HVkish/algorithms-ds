import sys

data = sys.stdin.read().split()
it = iter(data)

n = int(next(it))
m = int(next(it))

INF = 10 ** 9
d = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    d[i][i] = 0

for _ in range(m):
    u = int(next(it))
    v = int(next(it))
    w = int(next(it))
    if w < d[u][v]:
        d[u][v] = w
        d[v][u] = w

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]

best = 1
best_ecc = INF
for v in range(1, n + 1):
    ecc = max(d[v][1:n + 1])
    if ecc < best_ecc:
        best_ecc = ecc
        best = v

print(best)
