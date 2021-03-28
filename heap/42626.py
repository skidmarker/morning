import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        n_spicy = heapq.heappop(scoville)
        nn_spicy = heapq.heappop(scoville)
        scoville.append(n_spicy + (nn_spicy*2))
        answer += 1
        
    return answer