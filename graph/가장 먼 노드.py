from collections import defaultdict

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    visited = [0] * n
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        
    q = [1]
    visited[0] = 1
    
    while q:
        answer = len(q)
        for _ in range(len(q)):
            cur = q.pop(0)
            for node in graph[cur]:
                if visited[node-1] == 0:
                    visited[node-1] = 1
                    q.append(node)
        
    return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])