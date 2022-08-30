total = 0
totals = []
for i in range(10):
    N = int(input())
    total += N
    if total == 100:
        print(100)
        break
    else:
        totals.append(total)
else:
    min_v = 999999
    for j in range(len(totals)):
        if abs(totals[j] - 100) <= min_v:
            min_v = abs(totals[j] - 100)
            ans = totals[j]
    print(ans)
