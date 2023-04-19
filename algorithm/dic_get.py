# 카테고리별로 옷을 입어 위장할 수 있는 숫자
c = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
     ["green_turban", "headgear"]]
## 답 : 5

# 1. 딕셔너리 (hash table)


def solution(c):
    dict = {}  # type별 갯수
    for n, t in c:
        if t not in dict:
            dict[t] = 1
        else:
            dict[t] += 1

    result = 1
    for i in dict:
        result *= (dict[i] + 1)

    return result - 1


print(solution(c))

# 1-1. dict.get(값, 초기값)을 사용하여 맨 처음 발생할수 있는 키에러 방지



def solution2(c):
    dic = {}
    for n, t in c:
        dic[t] = dic.get(t, 0) + 1

    result = 1
    for i in dic:
        result *= (dic[i] + 1)

    return result - 1


print(solution2(c))

# 2. Counter() : dict의 구조
from collections import Counter

def solution3(c):
    counter = Counter([t for n, t in c])

    result = 1
    for i in counter:
        result *= (counter[i] + 1)

    return result - 1


print(solution3(c))
