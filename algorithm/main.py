# 외계 행성의 나이 : 각 자릿수 분리하기 : str()
def solution(age):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    num = list(map(int, str(age)))
    result = ''

    for i in num:
        result += a[i]
    return result


print(solution(23))

# 외계어 사전
spell = ["z", "d", "x"]
dic = ["def", "dww", "dzx", "loveaw"]

# 1. 순열
from itertools import permutations


def solution2(spell, dic):
    new = list(permutations(spell, len(spell)))
    for i in new:
        if ''.join(i) in dic:
            return 1
    ##else : return 2  for 반복문 안에서 return 2를 할 경우, 앞 부분에서 조건이 맞지 않으면 바로 return 2를 출력해 전체 i를 확인할 수 없다.
    return 2  ## for 반복문을 모두 확인한 후에 조건에 충족하지 않는다면 return 2


print(solution2(spell, dic))


# 2. set() - set() : 차집합
def solution3(spell, dic):

    for i in dic:
        if not set(i) - set(spell):
            return 1
    return 2


print(solution3(spell, dic))

# 2-1. list의 차집합
x = [1, 2, 6, 5]
y = [1, 2, 3, 4]
xy = []
for i in x:
    if i not in y:
        xy.append(i)

print(xy)
