# n개씩 끊어 2차원의 list로 만들기
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3


# 1. range(시작, 끝, 간격)
def solution(l, n):
    a = []
    for i in range(0, len(l), n):
        a.append(l[i:i + n])
    return a


print(solution(l, n))

# 2. numpy
import numpy as np


def solution2(l, n):
    new = np.reshape(l, (-1, n))
    return new.tolist()


print(solution2(l, n))
