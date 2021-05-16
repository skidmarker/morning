N = int(input())

start = dict()
end = []

answer = 0

for i in range(N):
    car = input()
    start[car] = i
for _ in range(N):
    end.append(input())

for i in range(N):
    for j in range(i + 1, N):
        if start[end[i]] > start[end[j]]:
            answer += 1
            break

print(answer)
