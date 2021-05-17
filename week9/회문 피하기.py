def main():
    n = int(input())
    s_lst = [input() for _ in range(n)]

    answer = []
    for s in s_lst:
        mid = len(s) // 2
        if len(s) % 2 == 0:
            if s[:mid] != s[: mid - 1 : -1]:
                answer.append("YES")
            else:
                if s[:mid] == "a" * mid:
                    answer.append("NO")
        else:
            if s[:mid] != s[:mid:-1]:
                answer.append("YES")
            else:
                if s[:mid] == "a" * mid:
                    answer.append("NO")

    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
