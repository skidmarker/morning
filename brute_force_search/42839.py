from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    result = []
    for i in range(1, len(numbers)+1):
        nums = list(map(''.join, permutations(numbers,i)))
        for num in list(set(nums)):
            if is_prime(int(num)):
                result.append(int(num))
    
    answer = len(set(result))
    return answer