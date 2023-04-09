# 삼각형 완성 조건 : 가장 긴 변 < 다른 두 변의 합
sides = [1, 2]  ## 답 1


# 1. range()
def solution(sides):
    result = 0
    # sides 안에 가장 긴 변이 있는 경우
    for i in range(1, max(sides)):
        if i + min(sides) > max(sides):
            result += 1

    # sides 안에 가장 긴 변이 없는 경우
    for i in range(max(sides), sum(sides)):
        if sum(sides) > i:
            result += 1

    return result


print(solution(sides))


# 1-1. list compression
def solution2(sides):
    n1 = len([i for i in range(1, max(sides)) if i + min(sides) > max(sides)])
    n2 = len([i for i in range(max(sides), sum(sides))])
    return n1 + n2


print(solution2(sides))


# 2. 공식
def solution3(sides):
    return 2 * min(sides) - 1


print(solution3(sides))
