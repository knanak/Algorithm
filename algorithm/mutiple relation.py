### 암호해독문제. code의 n의 배수번째 오는 문자가 암호
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



### 공 던지기 문제 : n명의 사람들이 한 칸씩 건너뛰며 공을 던지고 있다. k번째 던지는 사람은?
# list 안에서 k의 배수에 따라 돌기 때문에 나머지%를 활용할 수 있다고 생각



