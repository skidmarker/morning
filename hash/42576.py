def solution(participant, completion):
    answer = ''
    name_dict = {}
    for name in completion:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    
    for name in participant:
        if name not in name_dict or name_dict[name] == 0:
            answer = name
            break
        else:
            name_dict[name] -= 1
            
    return answer