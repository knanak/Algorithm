# 이진수 더하기 : 십진수로 더해주고, 다시 이진수로 바꾸기. 0b로 바꾸기
bin1 = "1001"
bin2 = "1111"


# 1. str[:] : 슬라이싱
def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    result = bin(a + b)
    return result[2:]


print(solution(bin1, bin2))


# 2. str.replace()
def solution2(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    result = bin(a + b)
    return result.replace('0b', '')


print(solution2(bin1, bin2))
