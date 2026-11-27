s = input().strip()

balance = 0
extra = 0
for c in s:
    if c == '(':
        balance += 1
    elif balance > 0:
        balance -= 1
    else:
        extra += 1

print(extra + balance)
