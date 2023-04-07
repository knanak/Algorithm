# 문자열 계산 : 문자열의 +, -를 이용하여 계산
my_string = "3 + 4"


# 1. range(시작, 끝, 간격)
def solution(my_string):
    s = my_string.split()
    result = int(s[0])
    for i in range(1, len(s), 2):
        if s[i] == '+':
            result += int(s[i + 1])
        else:
            result -= int(s[i + 1])

    return result


print(solution(my_string))


# 2. str.replace('-를', '-로')
def solution2(my_string):
    return sum([int(i) for i in my_string.replace('-', '+-').split('+')])


print(solution2(my_string))
