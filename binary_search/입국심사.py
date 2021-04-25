def solution(n, times):
    answer = 0
    
    times.sort()
    left = 1
    right = n * times[0]
    
    while left <= right:
        mid = (left + right) // 2
        people = n
        for time in times:
            people -= mid // time
            if people <= 0:
                answer = mid
                right = mid - 1
                break
        if people > 0:
            left = mid + 1
            
    return answer