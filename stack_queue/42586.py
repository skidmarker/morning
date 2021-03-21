import math

def solution(progresses, speeds):
    answer = []
    complete = []
    for i in range(len(speeds)):
        complete.append(math.ceil((100-progresses[i])/speeds[i]))
        
    day = complete[0]
    answer.append(1)
    for i in range(1, len(complete)):
        if complete[i] <= day:
            answer[-1] += 1
        else:
            answer.append(1)
            day = complete[i]
    return answer