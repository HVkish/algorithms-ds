import heapq
import sys

data = sys.stdin.read().split()
it = iter(data)

n = int(next(it))
m = int(next(it))
k = int(next(it))
capital = int(next(it))

cities = [int(next(it)) for _ in range(k)]

g = [[] for _ in range(n + 1)]
for _ in range(m):
    u = int(next(it))
    v = int(next(it))
    w = int(next(it))
    g[u].append((v, w))
    g[v].append((u, w))

INF = 10 ** 18
dist = [INF] * (n + 1)
dist[capital] = 0
pq = [(0, capital)]
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

res = sorted((dist[c], c) for c in cities)
for t, c in res:
    print(c, t)
