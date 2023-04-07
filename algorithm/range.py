# 잘라서 배열로 저장
my_str = "abc1Addfggg4556b"  # 답 : ["abc1Ad", "dfggg4", "556b"]
n = 6


# 1. range(시작, 끝, 간격)
def solution(my_str, n):
    result = []
    for i in range(0, len(my_str), n):
        if len(my_str[i:i + n]) >= 6:
            result.append(my_str[i:i + n])
        else:
            result.append(my_str[i:len(my_str)])

    return result


print(solution(my_str, n))


# 1-1. range를 초과해서 슬라이싱[]하더라도 에러 안남
def solution2(my_str, n):
    return [my_str[i:i + n] for i in range(0, len(my_str), n)]


print(solution2(my_str, n))


# 2.while문
def solution3(my_str, n):
    result = []
    while my_str:
        if len(my_str) >= n:
            result.append(my_str[:n])
            my_str = my_str[n:]
        else:
            result.append(my_str)
            my_str = ''
    return result


print(solution3(my_str, n))
