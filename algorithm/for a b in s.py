'''
최소 직사각형
명함의 가로, 세로 크기를 고려하여 만드는 지각의 최소 넓이는?
'''

s = [[60, 50], [30, 70], [60, 30], [80, 40]]  ## 답 : 4000


# 1. max(), min()
def solution(s):
    row = []
    col = []
    for i in s:
        row.append(max(i))
        col.append(min(i))

    return max(row) * max(col)


print(solution(s))


# 2. 반복문으로 2차원 리스트 값 가져오기
def solution2(s):
    row = 0
    col = 0
    for a, b in s:
        if a < b:
            a, b = b, a

        row = max(row, a)
        col = max(col, b)

    return row * col


print(solution2(s))
