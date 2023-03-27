# 암호해독문제. code의 n의 배수번째 오는 문자가 암호
list = "dfjardstddetckdaccccdegk"
num = 4


# 1. ranage(시작, 끝, 간격)
def solution(cipher, code):
    result = ''
    for i in range(code, len(cipher) + 1, code):
        result += cipher[i - 1]
    return result


# 2. list[시작:끝:간격]
def solution2(cipher, code):
    return cipher[code - 1::code]


# 3. 나머지 : 배수관계인 경우, 나머지가 0
def solution3(cipher, code):
    result = ''
    for i in range(code, len(cipher) + 1):
        if i % code == 0:
            result += cipher[i - 1]
    return result


solution(list, num)
solution2(list, num)
solution3(list, num)
