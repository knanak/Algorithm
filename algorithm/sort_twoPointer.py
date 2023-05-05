'''
리스트안의 원소의 합이 x가 되는 경우의 수 구하기
'''

from sys import stdin

n = int(input())
a = list(map(int, stdin.readline().split()))
x = int(input())

# 1. if in 조건문
# cnt = 0
# for i in a:

#     if (x - i) in a:
#         cnt += 1

# print(int(cnt / 2))

#2. 정렬후, 투포인터 사용 : 기준이 st
# a.sort()
# st, end, cnt = 0, n - 1, 0
# while st < end:
#     if a[st] + a[end] == x:
#         cnt += 1
#         st += 1
#     elif a[st] + a[end] < x:
#         st += 1
#     else:
#         end -= 1

# print(cnt)

# 2-1. 투포인터의 기준이 end
a.sort()
st, end, cnt = 0, n - 1, 0
while st < end:
    tmp = a[st] + a[end]
    if tmp == x:
        cnt += 1
    elif tmp < x:
        st += 1
        continue  ## contine를 써주는 이유
    end -= 1

print(cnt)
