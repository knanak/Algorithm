# 개미전사 문제 : 최소 1칸 이상 떨어진 창고를 약탈하여 최대 식량 얻기

#ⓐ블록단위로 생각해서 풀기
list = list(map(int, input().split()))
result = []

for i in range(len(list)):  ## 0 <= i <= n-1
    if i + 2 <= len(list) - 1:  ## 0부터 시작하므로 -1해줘야
        k = list[i] + max(list[i + 2:])
        result.append(k)

print(max(result))

#ⓑ다이나믹 이용해 풀기
list = list(map(int, input().split()))

d = [0] * len(list)
d[0] = list[0]
d[1] = max(list[0:2])

for i in range(2, len(list)):
    d[i] = max(d[i - 1], d[i - 2] + list[i])

print(d[len(list) - 1])
