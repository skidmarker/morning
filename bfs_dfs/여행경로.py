def solution(tickets):
    answer = []
    tickets.sort(reverse=True)
    routes = {}
    for dep, arr in tickets:
        if dep in routes:
            routes[dep].append(arr)
        else:
            routes[dep] = [arr]

    start = ["ICN"]

    while start:
        tmp = start[-1]
        if tmp not in routes or len(routes[tmp]) == 0:
            answer.append(start.pop())
        else:
            start.append(routes[tmp].pop())

    answer.reverse()
    return answer
