'''여행경로
'''


#1. dfs
def solution(tickets):
    answer = []

    visited = [False] * len(tickets)

    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                # idx를 돌면서, 해당하는 값을 모두 찾을 수 있도록 False
                visited[idx] = False

    dfs("ICN", ["ICN"])

    answer.sort()

    return answer[0]

