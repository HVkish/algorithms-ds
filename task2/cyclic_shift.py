from substring_search import kmp


def main():
    s = input().strip()
    t = input().strip()
    n = len(s)

    ans = -1
    if len(t) == n:
        for pos in kmp(s + s, t):
            if 1 <= pos <= n:
                k = n - pos
                if ans == -1 or k < ans:
                    ans = k
    print(ans)


if __name__ == "__main__":
    main()
