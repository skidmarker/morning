def solution(n, lost, reserve):
    answer = 0
    clothes = [1] * n
    clothes.append(-1)
    
    for i in lost:
        clothes[i-1] -= 1
    for i in reserve:
        clothes[i-1] += 1
        
    for i in range(n):
        if clothes[i] == 0:
            if clothes[i-1] > 1:
                clothes[i] += 1
                clothes[i-1] -= 1
            elif clothes[i+1] > 1:
                clothes[i] += 1
                clothes[i+1] -= 1
                
    answer = n - clothes.count(0)
    return answer