# 숫자를 붙여서 가장 큰 수 만들기
numbers = [3, 30, 34, 5, 9]
numbers = list(map(str, numbers))
numbers.sort(key=lambda x: x * 3, reverse=True)
print(str(int(''.join(numbers))))
