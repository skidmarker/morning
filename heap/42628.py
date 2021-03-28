def solution(operations):
    answer = []

    result = []
    for operation in operations:        
        if operation.startswith('I '):
            result.append(int(operation[2:]))
            
        if operation == ('D -1'):
            if len(result) == 0: continue
            result.pop(0)
        elif operation == ('D 1'):
            if len(result) == 0: continue
            result.pop()
        result.sort()

    if len(result) == 0:
        answer = [0, 0]
    else:
        answer += (result[-1], result[0])
        
    return answer