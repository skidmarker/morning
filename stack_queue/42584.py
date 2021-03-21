from collections import deque

def solution(prices):
    answer = []
    
    que = deque(prices)
    while que:
        time = 0
        cur = que.popleft()
        for price in que:
            if cur <= price:
                time += 1
            else:
                time += 1
                break
        
        answer.append(time)
        
    return answer