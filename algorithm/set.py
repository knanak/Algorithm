'''
체육복 빌려주기
'''
n = 5
l = [2, 4]
r = [1, 3, 5]  # 답 : 5


# 1. set()을 통한 차집합 : 공통요소 제거
def solution(n, l, r):
    r = set(r) - set(l)
    l = set(l) - set(r)

    for i in r:
        if i - 1 in l:
            l.remove(i - 1)
        elif i + 1 in l:
            l.remove(i + 1)

    return n - len(l)


print(solution(n, l, r))
