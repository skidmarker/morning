def solution(name):
    answer = 0
    
    change = []
    for alphabet in name:
        change.append(min(ord(alphabet)-ord('A'), ord('Z')-ord(alphabet)+1))
    
    i = 0
    while True:
        answer += change[i]
        change[i] = 0
        if sum(change) == 0:
            break
            
        left, right = 1, 1
        while change[i-left] == 0:
            left += 1
        while change[i+right] == 0:
            right += 1
            
        answer += min(left, right)
        i += -left if left < right else right
        
    return answer