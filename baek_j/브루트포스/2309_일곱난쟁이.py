heights = []
total = 0
for _ in range(9):
    n = int(input())
    heights.append(n)
    total += n
heights.sort()
for i in range(9):
    for j in range(i + 1, 9):
        if total - heights[i] - heights[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(heights[k])
            exit()

# for i in range(9):
#     total = 0
#     ans = []
#     for j in range(7):
#         total += heights[(i + j) % 9]
#         ans.append(heights[(i + j) % 9])
#         if total > 100:
#             break
#     if total == 100:
#         break
# for i in sorted(ans):
#     print(i)