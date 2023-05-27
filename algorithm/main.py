'''
피로도. 전체 n의 갯수가 많지 않을 경우, 완전 탐색 가능성
'''
from itertools import permutations
def solution(k,d):
  answer=0
  for pm in permutations(d, len(d)):
    hp=k
    cnt=0

    for p in pm:
      if hp >= pm[0]:
        hp-=pm[1]
        cnt+=1

    if cnt > answer :
      answer=cnt  

  return answer

