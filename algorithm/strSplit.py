# 컨트롤 Z : Z가 나오면 이전 요소를 빼준다.
s = "10 Z 20 Z 1"


#1. 단순히 빼주기
def solution(s):
    s = s.split()
    result = 0
    for i in range(len(s)):
        if s[i] == 'Z':
            result -= int(s[i - 1])
        else:
            result += int(s[i])
    return result


print(solution(s))


#2. stack 이용하기 : 최근값을 빼줌
def solution1(s):
    stack = []
    for i in s.split():
        if i == 'Z':
            if stack:
                stack.pop()
        else:
            stack.append(int(i))

    return sum(stack)


print(solution1(s))