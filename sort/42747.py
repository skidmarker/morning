def solution(citations):
    answer = 0
    
    n = len(citations)
    citations.sort(reverse=True)
    
    while answer < n and citations[answer] >= answer+1:
        answer += 1
    
    return str(int(answer))
