'''
문제를 가장 많이 맞힌 사람은?
'''

a = [1, 3, 2, 4, 2]  # 정답 : [1,2,3]


def solution(a):
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    r = [0] * 3

    for idx, i in enumerate(a):
        if i == n1[idx % len(n1)]:
            # 리스트의 인덱스를 통해 특정 조건이 만족한 경우의 수를 누적
            r[0] += 1

        if i == n1[idx % len(n2)]:
            r[1] += 1

        if i == n1[idx % len(n3)]:
            r[2] += 1

    k = []
    for idx, i in enumerate(r):
        if i == max(r):
            k.append(idx + 1)

    return k


print(solution(a))