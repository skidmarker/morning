def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: x*4)
    answer = ''
    
    for i in numbers:
        answer += i
    return answer
