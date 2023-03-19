# 프로그래머스 옹알이 문제 : 아기가 말할 수 있는 단어의 수
# ⓐ 순열로  풀기
from itertools import permutations


def solution(babbling):
    answer = 0
    seek = ['aya', 'ye', 'woo', 'ma']
    word = []

    for i in range(len(seek)):
        new = permutations(seek, i)
        for j in new:
            word.append(''.join(j))

    for i in babbling:
        if i in word:
            answer += 1

    return answer


# ⓑ 정규식으로 풀기
import re


def solution2(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')  ## 패턴 만들기
    cnt = 0
    for i in babbling:
        if regex.match(i):
            cnt += 1
    return cnt
