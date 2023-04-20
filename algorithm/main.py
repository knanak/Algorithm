'''
랜선 자르기
k개의 랜선을 동일한 길이로 잘라 n개의 랜선을 만들 때, 최대길이는?
'''

from sys import stdin

k, n = map(int, stdin.readline().split())
kList = [int(stdin.readline()) for _ in range(k)]

st = 1  # 랜선의 최 길이
end = max(kList)

while st <= end:
    mid = (st + end) // 2
    ##count는 각 반복문마다 초기화되야 하므로 while문 안에 선언
    count = 0

    for i in range(k):
        count += kList[i] // mid

    ## mid+1되는 조건에 >=이 붙어 while의 종료조건을 설정
    if count >= n:
        st = mid + 1
    else:
        end = mid - 1

print(end)
