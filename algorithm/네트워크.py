'''
네트워크
'''
computers= [[1, 1, 0], 
            [1, 1, 0], 
            [0, 0, 1]]
n=len(computers)

#1. dfs : 컴퓨터에 연결된 네트워크를 모두 찾은 후, 다음 컴퓨터로 넘어가야 되므로 dfs가 적합
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1 
    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: 
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
      
        
print(solution(n, computers))


