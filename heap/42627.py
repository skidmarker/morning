def solution(jobs):
    answer = 0
    time = 0
    work_time = []
    
    jobs = sorted(jobs, key=lambda x: (x[1],x[0]))
    
    while jobs:
        n = len(jobs)
        for i in range(n):
            if jobs[i][0] <= time:
                start = jobs[i][0]
                work = jobs[i][1]
                del jobs[i]
                break

        if len(jobs) == n:
            time += 1   
        else:   
            work_time.append(time-start+work)
            time += work
        
    answer = sum(work_time) // len(work_time)
        
    return answer