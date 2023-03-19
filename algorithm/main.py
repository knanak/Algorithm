#살 수 있는 커피의 최대 갯수(몫)와 잔돈(나머지)
money, price = (10000, 3000)
a, b = divmod(money, price)

#7조각 피자를 n명이 먹으려면 몇 판 필요한가 : 필요한 피자의 갯수는 몫과 관련됨
n = 100
num = n // 7 + (1 if n % 7 else 0)

#array의 중앙값 출력
array = [2, 6, 9, 4, 3, 5, 7]
array.sort()
mid = len(array) // 2  ## array의 인덱싱이 0부터 시작하므로 len()+1 할 필요 없음
mid = array[mid]
