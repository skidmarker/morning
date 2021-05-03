def solution(N, number):
    answer = -1
    if N == number:
        return 1

    s = dict()
    for i in range(1, 9):
        s[i] = {int(str(N) * i)}

    for i in range(1, 9):
        for j in range(1, i):
            for num1 in s[j]:
                for num2 in s[i - j]:
                    s[i].add(num1 + num2)
                    s[i].add(num1 - num2)
                    s[i].add(num1 * num2)
                    if num2 != 0:
                        s[i].add(num1 // num2)

        if number in s[i]:
            answer = i
            break

    return answer
