# n개의 원소, k번 바꿔치기 후, a리스트 값들의 총합이 최대가 되도록

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 1) min(), max() 함수 이용
# for i in range(k):
#     am = a.index(min(a))
#     bm = b.index(max(b))
#     a[am], b[bm] = b[bm], a[am]

# print(sum(a))

# 2) .sort()이용
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
