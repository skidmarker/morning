def solution(priorities, location):
    pri_loc = []
    for i in range(len(priorities)):
        if i == location:
            pri_loc.append((priorities[i],1))
        else:
            pri_loc.append((priorities[i],0))
    
    work = []    
    while pri_loc:
        tmp_len = len(pri_loc)
        tmp = pri_loc[0]
        del pri_loc[0]
        
        for i in range(0, len(pri_loc)):
            if pri_loc[i][0] > tmp[0]:
                pri_loc.append(tmp)
                break
        
        if tmp_len != len(pri_loc):
            work.append(tmp)
        
    for i in range(len(work)):
        if work[i][1] == 1:
            answer = i

    return answer+1