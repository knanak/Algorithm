from sys import stdin

n, k = map(int, stdin.readline().split())
days = list(map(int, stdin.readline().split()))
d = []
# 1. 반복문 + sum()
for i in range(n - k):
    d.append(sum(days[i:i + k]))

print(max(d))

# 2. while + sum()
x, y = 0, k
while y <= n:
    d.append(sum(days[x:y]))
    x += 1
    y += 1

print(max(d))

# 3. 투 포인터
result = 0
for i in range(k):
    result += days[i]
max_t = result  # 예전 result

x, y = 0, k
while y <= n - 1:
    result = result + days[y] - days[x]  # 현재 result
    max_t = max(max_t, result)
    x += 1
    y += 1

print(max_t)