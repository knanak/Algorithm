# '''
# 암호 만들기 : c개 중 최소 한개의 모음 + 최소 두개의 자음으로 n번째로 구성된 암호 만들기
# '''

# n,c=map(int, input().split())
# cList=list(map(str, input().split()))
# cList.sort()
# result=[]
# v=['a', 'e', 'i', 'o', 'u']

# def back(st):
#   if len(result)== n:
#     cnt=0
#     for i in range(n):
#       if result[i] in v:
#         cnt+=1
#         if cnt != n :
#           print(''.join(result))
#           return


#   for i in range(st, c) :
#     result.append(cList[i])
#     back(i+1)
#     result.pop()

# back(0)

import sys


def back_tracking(idx):

    # 암호를 만들었을 때
    if len(answer) == l:
        # 모음, 자음 체크
        vo, co = 0, 0

        for i in answer :
            if i in consonant:
                vo += 1
            else:
                co += 1

        # 모음 1개 이상, 자음 2개 이상
        if vo >= 1 and co >= 2:
            print("".join(answer))

        return

    # 반복문을 통해 암호를 만든다.
    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(i + 1) # 백트래킹
        answer.pop()


l, c = map(int, sys.stdin.readline().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
consonant = ['a', 'e', 'i', 'o', 'u']
answer = []
back_tracking(0)
