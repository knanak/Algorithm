# 알파벳str을 int로 변경
n = "onetwothreefourfivesixseveneightnine"


#1. list.replace('-를', '-로')와 enumerate()
def solution(n):
    ch = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine'
    ]
    for idx, i in enumerate(ch):
        n = n.replace(i, str(idx))
    return int(n)


print(solution(n))


#1-1. list.replace('-를', '-로')와 list
def solution2(n):
    ch = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine'
    ]
    for i in range(len(ch)):
        n = n.replace(ch[i], str(i))
    return int(n)


print(solution2(n))


#2, list(dic.keys())
def solution3(numbers):
    dic = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    new = ''
    result = ''
    for i in numbers:
        new += i
        if new in list(dic.keys()):
            result += str(dic[new])
            new = ''
    return int(result)


print(solution3(n))
