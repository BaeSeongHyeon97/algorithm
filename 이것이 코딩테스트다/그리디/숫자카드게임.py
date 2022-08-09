# for i in range(n):
#     cards = list(map(int,input().split()))
#
# 11:45 /

# 여러개의 카드중 가장 높은 숫자가 쓰인 카드 한장 뽑
# N * M의 형태로 놓여있고 / N은 행(가로), M은 열(세로)
# 뽑고자 하는 카드가 포함된 행을 선택
# 선택된 행에서 가장 숫자가 낮은 카드를 뽑아
#---------------------------------------------------
# min 없이
n, m = map(int,input().split())
min_vals = []
result = 0
for i in range(n):
    card = list(map(int,input().split()))
    min_val = 10001
    for j in range(m):
        if card[j] < min_val:
            min_val = card[j]
    min_vals.append(min_val)

for k in range(n):
    if min_vals[k] > result:
        result = min_vals[k]
print(result)

#---------------------------------
# min으로
n, m = map(int,input().split())
result = 0
for i in range(n):
    card = list(map(int, input().split()))
    min_val = min(card)
    result = max(result, min_val)

print(result)













