# i에서 j까지의 k의 갯수
i = 1
j = 13
k = 1


# 1. 안에 있는지 확인 for i in A , if i in A
def solution(i, j, k):
    count = 0
    for a in range(i, j + 1):
        if str(k) in str(a):
            for b in str(a):
                if b == str(k):
                    count += 1
    return count


print(solution(i, j, k))


# 2. list.count('값')
def solution2(i, j, k):
    result = 0
    for a in range(i, j + 1):
        result += str(a).count(str(k))
    return result


print(solution2(i, j, k))


# 3. sum()
def solution3(i, j, k):
    return sum([str(x).count(str(k)) for x in range(i, j + 1)])


print(solution3(i, j, k))


def solution4(i, j, k):
    return sum(map(lambda x: str(x).count(str(k)), range(i, j + 1)))


print(solution4(i, j, k))
