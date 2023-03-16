import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
d = [inf] * (n + 1)

for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  ## a노드에서 b노드로 가는 cost(c)


def dikstra(start):
    q = []  ## (노드까지의 최단거리, 노드)
    heapq.headpush(q, (0, start))
    d[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if d[now] < dist:
            continue

        for i in graph[now]:  # i는 now노드와 인접한 노드들. i= (이동할 노드, 비용)
            cost = dist + i[1]

            if cost < d[i[0]]:
                d[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dikstra(start)

## 모든 노드로 가기 위한 최단거리 출력하기
for i in range(1, n + 1):
    if d[i] == inf:
        print('nothing')
    else:
        print(d[i])
