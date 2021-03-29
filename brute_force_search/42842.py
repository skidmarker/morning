def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for row in range(1,total):
        if total % row == 0:
            column = total / row
            if row >= column and (row-2)*(column-2) % yellow == 0:
                answer = [row, column]
                break
    return answer