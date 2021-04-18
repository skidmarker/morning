def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    queue = [begin]
    while True:
        tmp_queue = []
        for word in queue:
            if word == target:
                return answer
            for idx in range(len(words) - 1, -1, -1):
                tmp_word = words[idx]
                diff = sum([x != y for x, y in zip(word, tmp_word)])
                if diff == 1:
                    tmp_queue.append(words.pop(idx))
        if not tmp_queue:
            return 0
        queue = tmp_queue
        answer += 1
