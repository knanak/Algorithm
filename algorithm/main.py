# 진료순서 정하기 : 응급도
e = [4, 1, 3]
# 1. list.index()와 sorted() : o(n), o(n logn)


def solution(e):
    num = sorted(e, reverse=True)
    new = []
    for i in e:
        new.append(num.index(i) + 1)
    return new


print(solution(e))

#1-1. 리스트 안에서 반복문 돌리기


def solution2(e):
    num = sorted(e, reverse=True)
    return [num.index(i) + 1 for i in e]


print(solution2(e))

# 2. dict
