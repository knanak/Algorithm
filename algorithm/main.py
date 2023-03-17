# 프로그래머스 옹알이 문제 : 아기가 말할 수 있는 단어의 수
# ⓐ순열로  풀기
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
