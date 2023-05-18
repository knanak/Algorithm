'''
단어변환
'''
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque


def solution(begin, target, words):

    q = deque()
    q.append([begin, 0])
    v = [0 for i in range(len(words))]

    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
            break
        else:
            for i in range(len(words)):
                tmp = 0
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    q.append([words[i], cnt + 1])

    return
