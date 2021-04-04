def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x: x[2])
    connect = set([costs[0][0]])
    
    while len(connect) < n:
        for i in range(len(costs)):
            if costs[i][0] in connect and costs[i][1] in connect:
                continue
                
            if costs[i][0] in connect or costs[i][1] in connect:
                connect.update([costs[i][0], costs[i][1]])
                answer += costs[i][2]
                costs[i] = [-1, -1, -1]
                break
                
    return answer