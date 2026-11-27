def kmp(text, pattern):
    if not pattern:
        return []

    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j

    res = []
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            res.append(i - len(pattern) + 1)
            j = pi[j - 1]
    return res


def main():
    s = input().strip()
    t = input().strip()
    print(*kmp(s, t))


if __name__ == "__main__":
    main()
