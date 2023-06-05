'''
차이를 최대로
'''

n=int(input())
nList=list(map(int, input().split())) 
result=[]  ## ## nList의 요소가 들어옴
sum_max = []

def back(st): ## 인자로는 인덱스가 들어옴
  if len(result)==n:
    summ=0
    for i in range(len(result)-1):
      summ+=abs(result[i]-result[i+1])
      
    sum_max.append(summ)
    return

  for i in range(st, n):
    result.append(nList[i])
    back(i+1)
    result.pop()
    print(result)

back(0)
print(max(sum_max))