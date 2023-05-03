'''
리스트안의 원소의 합이 x가 되는 경우의 수 구하기
'''

from sys import stdin

n = int(input())
a = list(map(int, stdin.readline().split()))
x = int(input())

# 1. if in 조건문
cnt = 0
for i in a:

    if (x - i) in a:
        cnt += 1

print(int(cnt / 2))

#2. 정렬후, 투포인터 사용
a.sort()
st, end, cnt = 0, n - 1, 0
while st < end:
    if a[st] + a[end] == x:
        cnt += 1
        st += 1
    elif a[st] + a[end] < x:
        st += 1
    else:
        end -= 1

print(cnt)
