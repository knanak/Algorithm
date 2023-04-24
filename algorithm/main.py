'''
카펫의 가로 > 세로 구하기
ⓐ 총 너비와 가로, 세로길이의 관계는 배수, 약수 관계이다.
ⓑ 기준(미지수)를 뭘로 설정할지 정하기
'''
brown = 8
yellow = 1  # 정답 : [3, 3]


# 1. 나머지와 몫을 사용. 총 너비의 가로와 세로 길이를 기준으로 삼음
def solution(b, y):
    size = b + y
    for i in range(3, b):  # 샌드위치 구조가 되려면 세로 3개가 필요
        if size % i == 0:
            j = size // i
            if (i - 2)(j - 2) == y:
                return sorted([i, j], reverse=True)


print(solution(brown, yellow))


# 2. while 문으로 약수관계 구하기. yellow의 가로와 세로 길이를 기준으로
def solution2(b, y):
    def brown(v, h):
        return 2 (v + h) + 4

    v, h = 0, y
    while v <= h:
        v += 1
        h = y // v
        if brown(v, h) == brown:
            return [h + 2, v + 2]


print(solution2(brown, yellow))


# 3. 둘레의 길이. yellow의 가로와 세로 길이를 기준으로
def solution3(b, y):
    for i in range(3, int(y**0.5) + 1):
        if y % i == 0:
            j = y // i
            if 2 (i + j) + 4 == b:
                return [j + 2, i + 2]


print(solution3(brown, yellow))
