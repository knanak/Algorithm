# 가장 큰 수를 찾고 그때의 index를 list로 반환하기
list = [2, 5, 1, 7, 5, 8]


# 1. list에서 값으로 index 찾기
def solution(array):
    return [max(array), list.index(max(array))]


# 2. sort()와 sorted()의 차이
def solution2(array):
    a = sorted(array)
    return [a[-1], array.index(a[-1])]
