def solution(genres, plays):
    answer = []
    
    play_dict = {}
    total = {}
                
    for i in range(0, len(plays)):
        if genres[i] in play_dict:
            play_dict[genres[i]] += [(plays[i], i)]
            total[genres[i]] += plays[i]
        else:
            play_dict[genres[i]] = [(plays[i], i)]
            total[genres[i]] = plays[i]
            
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)
    
    for key in total:
        play_list = play_dict[key[0]]
        play_list = sorted(play_list, key=lambda x: (-x[0],x[1]))
        
        for i in range(len(play_list)):
            if i == 2:
                break
            answer.append(play_list[i][1])
    
    
    return answer