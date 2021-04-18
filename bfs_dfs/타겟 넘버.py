def dfs(lst, numbers, target, size):
    answer = 0

    if len(lst) == size:
        if sum(lst) == target:
            return 1
        else:
            return 0
    else:
        tmp = numbers.pop(0)
        for i in [1, -1]:
            lst.append(tmp * i)
            answer += dfs(lst, numbers, target, size)
            lst.pop()
        numbers.append(tmp)
        return answer


def solution(numbers, target):
    answer = 0
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))
    return answer
