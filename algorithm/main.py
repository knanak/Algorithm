from sys import stdin

n = int(input())
x = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
v = [[False] * n for _ in range(n)]
each = 0
result = []

dy = [1, 0, -1, -0]
dx = [0, 1, 0, -1]
print(x[0][1])
print(v[0][1])


def dfs(y, x):
    global each
    each += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < n and 0 <= ny < n:
            if x[ny][nx] == 1 and v[ny][nx] == False:
                v[ny][nx] == True
                dfs(ny, nx)


for j in range(n):
    for i in range(n):
        if x[j][i] == 1 and v[j][i] == False:
            v[j][i] = True
            each = 0
            dfs(j, i)  # -> each(1로 연결된 갯수)가 나오게됨
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)
