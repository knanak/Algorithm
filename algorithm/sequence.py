# 다음에 올 숫자. list는 등비(공비!=0) or 등차 수열로 되어 있음


def solution(common):
    ## -로 먼저 값이 0인 경우를 제외해야 한다.
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    elif common[1] / common[0] == common[2] / common[1]:
        return common[-1] * (common[1] / common[0])


