def quick_sort(a):
    a = a[:]
    _sort(a, 0, len(a) - 1)
    return a


def _sort(a, lo, hi):
    if lo >= hi:
        return
    i = lo
    j = hi
    pivot = a[(lo + hi) // 2]
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    _sort(a, lo, j)
    _sort(a, i, hi)
