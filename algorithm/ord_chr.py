# 문자열 정렬 : 소문자로 변환한 후, 오름차순(abc~)
s = "heLLo"


#1. 대문자/소문자 변환, sorted() : 문자열정렬, return
def solution(s):
    so = sorted(s.lower())
    return ''.join(so)


print(solution(s))
#2. 아스키코드로 변환 : ord('문자'), chr(숫자)
# ord('A')==65, ord('Z')==90,  A-a 차이는 32
# ord('a')==97, ord('z')==122, a-z 차이는 25


def solution2(s):
    for i in s:
        if ord('A') <= ord(i) <= ord('Z'):
            s = s.replace(i, chr(ord(i) + 32))
    return ''.join(sorted(s))


print(solution2(s))
