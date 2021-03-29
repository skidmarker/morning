def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    f_cnt = 0
    s_cnt = 0
    t_cnt = 0
    for i in range(len(answers)):
        if answers[i] == first[i%len(first)]:
            f_cnt += 1
        if answers[i] == second[i%len(second)]:
            s_cnt += 1
        if answers[i] == third[i%len(third)]:
            t_cnt += 1
        
    max_ans = max(f_cnt, s_cnt, t_cnt)
    
    if f_cnt == max_ans:
        answer.append(1)
    if s_cnt == max_ans:
        answer.append(2)
    if t_cnt == max_ans:
        answer.append(3)
    
    return answer