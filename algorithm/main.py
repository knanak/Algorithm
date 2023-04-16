# 올바른 괄호 ()일 경우, True
s = "(())()"  # 정답 : 	true


# 1. 반복문으로 할 경우, 시간초과 오류가 남 : len(s)가 10^5로 시간복잡도가 o(n^2)인 방법을 사용하면 안됨
# (1) str = str.replace('-를 ', '-로')
def solution(s):
    while '()' in s:
        s = s.replace(
            '()', ''
        )  # replace의 시간복잡도 : o(문자열의 길이 * (교체할 문자열의 길이 + 교체되는 문자열의 길이/교체할 문자열의 길이))
    if s:
        return False
    return True


print(solution(s))


# 2. stack.append() 나 stack.pop()은 o(1)의 시간복잡도가 걸리므로 빠름
# (2) stack 구조 이용하기
def solution2(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False  # )이 남는 경우
    if stack:
        return False  # (이 남는 경우
    return True


print(solution2(s))


# (3) '('와 ')'의 갯수를 비교하기. 짝이 맞으려면 총합이 0이 되어야
def solution3(s):
    result = 0
    for i in s:
        if i == '(':
            result += 1
        else:
            if result > 0:
                result -= 1
            else:
                return False  # )이 남는 경우

    if result > 0:  # (이 남는 경우
        return False
    return True


print(solution3(s))

# (4) deque
from collections import deque


def solution4(s):
    q = deque()
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if q:
                q.popleft()
            else:
                return False

    return len(q) == 0


print(solution4(s))
