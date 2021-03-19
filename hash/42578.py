def solution(clothes):
    answer = 1
    clothse_dict = {}
    
    for kind in clothes:
        if kind[1] in clothse_dict:
            clothse_dict[kind[1]] += 1
        else:
            clothse_dict[kind[1]] = 1
            
    for val in clothse_dict.values():
        answer *= (val+1)
        
    answer -= 1
    
    return answer