from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

data = list(map(int, input().split()))

print("bubble:", bubble_sort(data))
print("merge: ", merge_sort(data))
print("quick: ", quick_sort(data))
